# send_emails.py

import pandas as pd
import smtplib
import time
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email_template import get_subject, get_body

# Load environment variables
load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
RESUME_PATH = os.getenv("RESUME_PATH", "Taha_Kotwal_Resume.pdf") 
CSV_PATH = "hr_contacts.csv"

def send_email(to_email, subject, body, attachment_path):
    print("Email_address:", EMAIL_ADDRESS)
    print("Email_password:", EMAIL_PASSWORD)
    print("Resume_path:", RESUME_PATH)
    
    # Check if resume file exists
    if not os.path.exists(attachment_path):
        raise FileNotFoundError(f"Resume file not found: {attachment_path}")
    
    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    with open(attachment_path, "rb") as file:
        attach = MIMEApplication(file.read(), _subtype="pdf")
        attach.add_header("Content-Disposition", "attachment", filename=os.path.basename(attachment_path))
        msg.attach(attach)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

def main():
    # Validate environment variables
    if not EMAIL_ADDRESS:
        print("❌ EMAIL_ADDRESS not found in .env file")
        return
    
    if not EMAIL_PASSWORD:
        print("❌ EMAIL_PASSWORD not found in .env file")
        return
    
    if not os.path.exists(RESUME_PATH):
        print(f"❌ Resume file not found: {RESUME_PATH}")
        print("Please check the RESUME_PATH in your .env file")
        return
    
    df = pd.read_csv(CSV_PATH)

    for _, row in df.iterrows():
        hr_name = row["hr_name"]
        company_name = row["company_name"]
        to_email = row["email"]

        subject = get_subject(company_name)
        body = get_body(hr_name, company_name)

        try:
            send_email(to_email, subject, body, RESUME_PATH)
            print(f"✅ Sent to {hr_name} at {company_name} ({to_email})")
            time.sleep(5)
        except Exception as e:
            print(f"❌ Failed to send to {to_email}: {e}")

if __name__ == "__main__":
    main()
