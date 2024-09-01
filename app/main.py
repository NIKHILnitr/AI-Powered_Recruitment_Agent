



from flask import Flask, request, render_template, jsonify
import os
import docx2txt
import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from twilio.rest import Client  # For sending SMS
from datetime import datetime
from huggingface_hub import InferenceClient
import json

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Set the Hugging Face token
os.environ["HF_TOKEN"] = "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"

repo_id = "microsoft/Phi-3-mini-4k-instruct"  # Adjust model as needed
llm_client = InferenceClient(
    model=repo_id,
    timeout=120,
)

def call_llm(inference_client: InferenceClient, prompt: str):
    response = inference_client.post(
        json={
            "inputs": prompt,
            "parameters": {"max_new_tokens": 200},
            "task": "text-generation",
        },
    )
    response_json = json.loads(response.decode())
    if isinstance(response_json, list) and len(response_json) > 0:
        generated_text = response_json[0].get("generated_text", "Text key not found")
        
        # Clean up the response to only include the answer
        answer_start = generated_text.lower().find("answer: ")
        if answer_start != -1:
            return generated_text[answer_start + len("answer: "):].strip()
        
        # Default return if no specific instruction found
        return generated_text.strip()
    
    return "Response format error"

# Function to extract text from PDF files
def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text

# Function to extract text from DOCX files
def extract_text_from_docx(file_path):
    return docx2txt.process(file_path)

# Function to extract text from TXT files
def extract_text_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Function to determine the correct extraction method based on file type
def extract_text(file_path):
    if file_path.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        return extract_text_from_docx(file_path)
    elif file_path.endswith('.txt'):
        return extract_text_from_txt(file_path)
    else:
        return ""

# Function to send SMS notification
def send_sms_notification(phone_number, message_body):
    account_sid = 'ACfa64b493b25c8d19dd14b1686074eea7'
    auth_token = 'b29b1bae9259d57e03daa699bafc7ac2'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message_body,
        from_='+15104919452',
        to=phone_number
    )

    print(f"Notification sent to {phone_number}: {message.sid}")

@app.route('/')
def index():
    return render_template('matchresume.html')

@app.route('/matcher', methods=['POST'])
def matcher():
    job_description = request.form['job_description']
    recruiter_phone_number = request.form['recruiter_phone_number']
    candidate_phone_numbers_raw = request.form['candidate_phone_numbers']
    interview_date = request.form['interview_date']
    online_meet_link = request.form['online_meet_link']
    resume_files = request.files.getlist('resumes')

    # Process candidate phone numbers
    candidate_phone_numbers = [num.strip() for num in candidate_phone_numbers_raw.split(',') if num.strip()]
    
    resumes = []
    for resume_file in resume_files:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], resume_file.filename)
        resume_file.save(filename)
        resumes.append(extract_text(filename))
    
    if not resumes or not job_description or not recruiter_phone_number or not interview_date or not online_meet_link or not candidate_phone_numbers:
        return render_template('matchresume.html', message="Please upload resumes, enter a job description, provide all required information.")
    
    if len(candidate_phone_numbers) < len(resumes):
        return render_template('matchresume.html', message="Number of candidate phone numbers is less than the number of resumes uploaded.")
    
    # Vectorize job description and resumes
    vectorizer = TfidfVectorizer().fit_transform([job_description] + resumes)
    vectors = vectorizer.toarray()

    # Calculate cosine similarities
    job_vector = vectors[0]
    resume_vectors = vectors[1:]
    similarities = cosine_similarity([job_vector], resume_vectors)[0]

    # Get top 5 resumes and their similarity scores
    top_indices = similarities.argsort()[-5:][::-1]
    top_resumes = [resume_files[i].filename for i in top_indices]
    similarity_scores = [round(similarities[i], 2) for i in top_indices]
    shortlisted_candidates = [candidate_phone_numbers[i] for i in top_indices]

    # Format interview date
    interview_date_obj = datetime.strptime(interview_date, '%Y-%m-%dT%H:%M')
    formatted_date = interview_date_obj.strftime('%A, %B %d, %Y at %I:%M %p')

    # Message body for the recruiter
    recruiter_message_body = f"Top matching resumes:\n"
    for i in range(len(top_resumes)):
        recruiter_message_body += f"{top_resumes[i]} (Similarity Score: {similarity_scores[i]})\n"
    recruiter_message_body += f"\nScheduled Interview Date and Time: {formatted_date}\nOnline Meet Link: {online_meet_link}"

    # Send a notification via SMS to the recruiter
    send_sms_notification(recruiter_phone_number, recruiter_message_body)

    # Message body for the candidates
    candidate_message_body_template = (
        f"Congratulations! You have been shortlisted for an interview.\n"
        f"Scheduled Interview Date and Time: {formatted_date}\n"
        f"Online Meet Link: {online_meet_link}"
    )

    # Send a notification via SMS to each shortlisted candidate
    for candidate_phone_number in shortlisted_candidates:
        send_sms_notification(candidate_phone_number, candidate_message_body_template)

    return render_template('matchresume.html', message="Top matching resumes and notifications have been sent.", top_resumes=top_resumes, similarity_scores=similarity_scores)


@app.route('/ask', methods=['POST'])
def ask():
    question = request.form['question']
    response = call_llm(llm_client, question)
    return jsonify({"response": response})

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)




