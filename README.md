# 📧 Bulk Job Application Email Sender

This tool allows you to send personalized job application emails with your resume to a list of HR contacts from a CSV file.

---

## 🚀 Features

- Reads HR names, emails, and companies from CSV
- Sends personalized emails with your resume
- Uses Gmail (with app password) securely via `.env`
- Modular code with `email_template.py`

---

## 🔧 Setup

1. Clone this repo  
2. Create a virtual environment  
3. Install dependencies  
4. Add `.env` file  
5. Run `send_emails.py`

---

## 🧪 Environment

```bash
python -m venv venv
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate        # Windows
pip install -r requirements.txt
