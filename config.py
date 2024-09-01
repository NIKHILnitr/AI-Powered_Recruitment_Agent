# config.py

class Config:
    SECRET_KEY = 'c24fe3e9ae3f84e29c7c2fdd122e0e4d'
    UPLOAD_FOLDER = 'uploads/'
    TWILIO_ACCOUNT_SID = 'ACfa64b493b25c8d19dd14b1686074eea7'
    TWILIO_AUTH_TOKEN = 'b29b1bae9259d57e03daa699bafc7ac2'
    TWILIO_PHONE_NUMBER = '+15104919452'
import secrets
secret_key = secrets.token_hex(16)
print(secret_key)

