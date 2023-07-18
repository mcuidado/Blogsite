
from smtplib import SMTP, SMTPAuthenticationError

EMAIL="recipient@email.com"
APP_PASS="PASS"

class Contact():
    def __init__(self, name, email, phone, message):
        self.name = name
        self.email = email
        self.phone = phone
        self.message = message
    
    def send_email(self):
        with SMTP("smtp.gmail.com" ,port=587) as smtp:
            try:
                smtp.starttls()
                sender = smtp.login(user=EMAIL, password=APP_PASS)
            except SMTPAuthenticationError:
                print(f"{SMTPAuthenticationError.smtp_error}")
            else:
                msg_body = f"Name: {self.name}\nEmail: {self.email}\nPhone: {self.phone}\nMessage: {self.message}"
                msg = f"Subject: New message from {self.name}\n\n{msg_body}"
                smtp.sendmail(
                    from_addr=EMAIL, 
                    to_addrs=EMAIL,
                    msg=msg
                )

        
