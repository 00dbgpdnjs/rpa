# Way2. Send an email to kor

import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage() # obj
msg["Subject"] = "테스트 메일입니다"
msg["From"] = EMAIL_ADDRESS
msg["To"] = "yuhyewon91@gmail.com"

# When sending e-mails to several people
# msg["To"] = "yuhyewon91@gmail.com, yuhyewon99@gmail.com"
# another way
# to_list = ["yuhyewon91@gmail.com", "yuhyewon99@gmail.com"]
# msg["To"] = ", ".join(to_list) # Refer to join_fn.py

# 참조 : Not recipients but people related to mail.
# msg["Cc"] = "nadocoding@gmail.com"

# 비밀참조 (blind carbon copy)
# msg["Bcc"] = "yuhyewon2@gmail.com"

msg.set_content("테스트 본문입니다")

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)