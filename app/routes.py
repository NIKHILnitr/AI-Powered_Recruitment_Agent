# app/routes.py

from flask import render_template, request
from .utils import send_sms

# Example of sending an SMS after matching resumes or scheduling an interview
@main_bp.route('/send-sms', methods=['POST'])
def send_sms_route():
    candidate_phone = request.form['phone']
    message_body = request.form['message_body']
    sms_sid = send_sms(candidate_phone, message_body)
    return f"SMS sent successfully! Message SID: {sms_sid}"

