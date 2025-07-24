# 📧 Bulk Job Application Email Sender

This tool allows you to send personalized job application emails with your resume to a list of HR contacts from a CSV file.

---

## 🚀 Features

- Reads HR names, emails, and companies from CSV
- Sends personalized emails with your resume attachment
- Uses Gmail with App Password for secure authentication
- Configurable resume path via environment variables
- Built-in validation for credentials and file paths
- Modular code structure with `email_template.py`
- Error handling with detailed feedback

---

## 📋 Prerequisites

1. **Gmail Account with 2-Factor Authentication**
2. **Gmail App Password** (not your regular password)
3. **Python 3.7+**

---

## 🔧 Setup

### 1. Clone and Navigate
```bash
git clone https://github.com/TahaKotwal12/hireme-mailer.git
cd hireme-mailer
```

### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate     # Linux/macOS
# venv\Scripts\activate      # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the project root:
```bash
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_16_character_app_password
RESUME_PATH=tr.pdf
```

### 5. Prepare Your Data
Update `hr_contacts.csv` with your target contacts:
```csv
hr_name,email,company_name,position
John Doe,hr@techcorp.com,Tech Corp,HR Manager
Jane Smith,careers@innovate.com,Innovate Inc,Talent Acquisition
```

### 6. Add Your Resume
Place your resume PDF in the project directory or update `RESUME_PATH` in `.env`

---

## 🎯 Usage

Run the email sender:
```bash
source venv/bin/activate
python3 send_emails.py
```

The script will:
- ✅ Validate your credentials and file paths
- ✅ Send personalized emails to each contact
- ✅ Show progress with detailed feedback
- ✅ Include a 5-second delay between emails

---

## ⚙️ Configuration

### Environment Variables (`.env`)
| Variable | Description | Example |
|----------|-------------|---------|
| `EMAIL_ADDRESS` | Your Gmail address | `your.email@gmail.com` |
| `EMAIL_PASSWORD` | Gmail App Password (16 chars) | `abcd efgh ijkl mnop` |
| `RESUME_PATH` | Path to your resume PDF | `tr.pdf` |

### CSV Format (`hr_contacts.csv`)
| Column | Required | Description |
|--------|----------|-------------|
| `hr_name` | Yes | HR person's name |
| `email` | Yes | HR person's email |
| `company_name` | Yes | Company name |
| `position` | Optional | HR person's position |

---

## 🔒 Setting Up Gmail App Password

1. **Enable 2-Factor Authentication**:
   - Go to [Google Account Security](https://myaccount.google.com/security)
   - Enable 2-Step Verification

2. **Generate App Password**:
   - Go to Google Account → Security → App passwords
   - Select "Mail" as the app
   - Copy the 16-character password
   - Add it to your `.env` file

---

## 📁 Project Structure

```
hireme-mailer/
├── send_emails.py          # Main script
├── email_template.py       # Email templates
├── hr_contacts.csv         # Contact list
├── requirements.txt        # Dependencies
├── .env                    # Environment variables
├── tr.pdf                  # Resume file
└── README.md              # This file
```

---

## 🚨 Troubleshooting

### Common Issues:

1. **"Username and Password not accepted"**
   - Make sure you're using Gmail App Password, not regular password
   - Verify 2-Factor Authentication is enabled

2. **"Resume file not found"**
   - Check the `RESUME_PATH` in your `.env` file
   - Ensure the file exists in the specified location

3. **"EMAIL_ADDRESS not found in .env file"**
   - Create the `.env` file with all required variables
   - Check for typos in variable names

---

## 📝 Customization

### Email Template
Edit `email_template.py` to customize:
- Email subject line
- Email body content
- Personal information

### Delay Between Emails
Modify the `time.sleep(5)` value in `send_emails.py` to change the delay

---

## 🛡️ Security Notes

- Never commit your `.env` file to version control
- Use Gmail App Passwords only
- Keep your credentials secure
- Test with a small batch first

---

## 📄 License

This project is for personal use. Please respect email sending limits and privacy policies.
