import smtplib
from email.message import EmailMessage
from config import smtp_sender, smtp_password

def send_email(to_email, subject, message, image_path = None):
    sender = smtp_sender
    password = smtp_password
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    
    try:
        server.login(sender, password)   
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = to_email
        msg.set_content(message)
        
        if image_path:
            with open(image_path, 'rb') as img:
                img_d = img.read()
                msg.add_attachment(img_d, maintype = 'image', subtype = 'jpg', filename = image_path)
        
        server.send_message(msg)
        return '200 OK' 
    except Exception as error:
        return f'Error {error}'
    
print(send_email('toksonbaevislam2004@gmail.com', 'Hello', 'Hello Islam', r'C:\Users\Islam\Desktop\aiogram\Без названия.png'))
       