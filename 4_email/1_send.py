# Way1. Send an email to only eng

import smtplib
from account import * # account.py

with smtplib.SMTP("smtp.gmail.com", 587) as smtp: # (gmail, port)
    smtp.ehlo() # 연결이 잘 수립됐는지 확인
    smtp.starttls() # 모든 내용이 암호화되어 전송
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) # Refer to account.py

    subject = "test mail"
    body = "mail body"

    msg = f"Subject: {subject}\n{body}" # standardized form  to send an email
    smtp.sendmail(EMAIL_ADDRESS, "yuhyewon91@gmail.com", msg) # (Me, To who, what)