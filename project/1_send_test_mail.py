# [신청 메일 양식] 구현

# 이 파일은 생략?해도됨. 내가 가상의 참여자를 만들어서, 참여자인척 내가 직접 나에게 보내서

import smtplib
from random import *
from account import *
from email.message import EmailMessage

# Fictitious Students
nicknames = ["유재석", "박명수", "정형돈", "노홍철", "조세호"]

# They send me an email to attend the lecture
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    for nickname in nicknames:
        msg = EmailMessage()
        msg["Subject"] = "파이썬 특강 신청합니다."
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = "yuhyewon91@gmail.com"

        # content = nickname + "/" + str(randint(1000, 9999))
        content = "/".join([nickname, str(randint(1000, 9999))])
        msg.set_content(content)
        smtp.send_message(msg)
        print(nickname + "님이 나에게 메일 발송 완료")