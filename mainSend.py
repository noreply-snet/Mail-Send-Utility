import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get SMTP configuration from environment variables
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))  # Default to 587 if not set
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD") 

# Mail Details
HTML_FILE_PATH = './templates/index.html'  # Replace with your HTML file path
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL") 
Subject = 'Testing HTML Mail'

# Function to send an HTML email
def send_html_email(to_email, subject, html_file_path):
    try:
        # Read the HTML content from the file
        with open(html_file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Set up the MIME message
        message = MIMEMultipart()
        message['From'] = EMAIL_ADDRESS
        message['To'] = to_email
        message['Subject'] = subject

        # Attach the HTML content to the email
        message.attach(MIMEText(html_content, 'html'))

        # Connect to the Gmail SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Start TLS encryption
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Log in to the server
            server.send_message(message)  # Send the email
            print(f"Email sent successfully to {to_email}")

    except Exception as e:
        print(f"Error sending email: {e}")


# Sending the email
send_html_email(RECIPIENT_EMAIL, Subject, HTML_FILE_PATH)
