import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(to_address, subject, body):
    msg = MIMEText(body) # Create a message
    msg['Subject'] = subject # Add a subject
    msg['From'] = os.getenv('MAIL_USERNAME') # Add a sender
    msg['To'] = to_address # Add a recipient

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls() # Secure the connection
        server.login(os.getenv('MAIL_USERNAME'), os.getenv('MAIL_PASSWORD')) # Login to the server
        server.sendmail(os.getenv('MAIL_USERNAME'), to_address, msg.as_string()) # Send the email
        print('Email sent successfully')


if __name__ == '__main__':
    to_address = 'adrian.sobczyk1@gmail.com'
    subject = 'Hello'
    body = 'This is a test email'
    send_email(to_address, subject, body)
