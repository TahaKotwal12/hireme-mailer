# email_template.py

def get_subject(company_name: str) -> str:
    return f"Application for Software Engineering Role at {company_name} – Taha Kotwal"

def get_body(hr_name: str, company_name: str) -> str:
    return f"""
Dear {hr_name},

I hope this message finds you well.

My name is Taha Kotwal, and I am a passionate and self-motivated Software Engineer with hands-on experience in developing scalable backend systems and full-stack applications using technologies such as Python (FastAPI), Spring Boot (WebFlux), React, and PostgreSQL. I am currently working at Cyber Manager Software Services, where I actively contribute to the development of SaaS-based services following modern software engineering principles and microservices architecture.

I am writing to express my strong interest in exploring software development opportunities at {company_name}. I bring a growth-oriented mindset, a deep interest in solving real-world problems, and a strong foundation in clean code, agile workflows, and collaborative team dynamics.

I am open to **relocating internationally** and can **join immediately** if the opportunity aligns. I truly value diverse teams and global collaboration, and I am confident in my ability to adapt quickly and contribute meaningfully.

Attached is my resume for your review. I would be grateful for the opportunity to connect and further discuss how my experience and aspirations align with your team’s needs.

Thank you for your time and consideration.

Warm regards,  
Taha Kotwal  
📧 tahakotwal54@gmail.com  
📱 +91 7219342962  
🔗 [LinkedIn](https://www.linkedin.com/in/taha-kotwal-894b911b5)  
🔗 [GitHub](https://github.com/TahaKotwal12)  
🔗 [Medium](https://medium.com/@tahakotwal54)
"""
