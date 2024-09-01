
# AI-Powered Recruitment Agent

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Project Overview

The **AI-Powered Recruitment Agent** is an intelligent system designed to automate and enhance the recruitment process. The AI agent can filter CVs/resumes, source candidates, send messages, provide shortlists, book interviews, and even answer questions from candidates and hiring managers. The goal of this project is to assist recruitment teams in finding the best candidates for job openings more efficiently and effectively than traditional methods.

By leveraging AI, the recruitment agent helps in automating repetitive tasks, allowing human recruiters to focus on more strategic aspects of the hiring process, such as interviewing and selecting the right candidates.

## Features

- **CV/Resume Filtering**: Automatically scans and evaluates resumes to identify the most suitable candidates.
- **Candidate Sourcing**: Identifies potential candidates from a pool of resumes and other sources.
- **Automated Messaging**: Sends personalized messages to both candidates and recruiters regarding shortlisting, interview schedules, and more.
- **Interview Scheduling**: Books interviews and sends calendar invites to both candidates and recruiters.
- **Chatbot Integration**: Provides answers to frequently asked questions from both candidates and hiring managers using an AI-powered chatbot.
- **Feedback Provision**: Offers insights and feedback on candidates to help recruiters make informed decisions.

## Technology Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **AI/ML**: Hugging Face Transformers, Mistral (fine-tuned for chatbot integration)
- **APIs**: Twilio API (for SMS notifications)
- **Version Control**: Git

## Installation and Setup

### Prerequisites

- Python 3.x
- Virtual Environment (optional but recommended)
- Twilio Account (for SMS functionality)

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/NIKHILnitr/AI-Powered_Recruitment_Agent.git
   cd ai-powered-recruitment-agent
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Create a `.env` file in the root directory and add the following:
     ```
     TWILIO_ACCOUNT_SID=your_twilio_account_sid
     TWILIO_AUTH_TOKEN=your_twilio_auth_token
     TWILIO_PHONE_NUMBER=your_twilio_phone_number
     ```

5. **Run the application:**
   ```bash
   python main.py
   ```

6. **Access the application:**
   Open your web browser and navigate to `http://127.0.0.1:5000`.

## Usage

### Uploading Resumes and Job Descriptions
1. Navigate to the "Resume Matcher" section.
2. Upload multiple resumes and provide the job description.
3. The system will automatically filter and shortlist candidates based on the provided job description.

### Messaging Candidates and Recruiters
1. Enter the phone numbers of candidates and recruiters.
2. The system will send automated messages with interview details and other relevant information.

### Scheduling Interviews
1. Select the interview date and time, and provide an online meeting link.
2. The system will book the interview and send calendar invites to both candidates and recruiters.

### Using the Chatbot
1. Navigate to the "Chatbot" section.
2. Ask questions related to the recruitment process, and the AI chatbot will provide answers.

## Project Structure

```
.
├── app/
│   ├── templates/
│   │   └── matchresume.html
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   ├── __init__.py
│   ├── main.py
├── config.py
├── .env
├── requirements.txt
├── README.md
├── LICENSE
└── Screenshot/
```

## Screenshots

![Screenshot 2024-09-01 121617](https://github.com/user-attachments/assets/ed723246-b494-487f-afa2-bae513ece68c)
![Screenshot 2024-09-01 121637](https://github.com/user-attachments/assets/2d7b393b-6ce2-4547-91c0-0471d6bd8ce4)
![Screenshot 2024-09-01 121649](https://github.com/user-attachments/assets/3a7bbe23-8f8b-4f43-a06d-76c22b1f9cfe)



## Future Improvements

- **Enhanced AI Algorithms**: Improve the resume matching algorithms for better accuracy.
- **Multi-language Support**: Extend the chatbot and interface to support multiple languages.
- **Analytics Dashboard**: Provide a dashboard for recruiters to visualize the recruitment process and candidate analytics.
- **Email Notifications**: Integrate email notifications along with SMS for a more comprehensive communication strategy.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments

- Special thanks to [Hugging Face](https://huggingface.co/) for their amazing AI models.
- Thanks to [Twilio](https://www.twilio.com/) for providing the communication API.
```


