import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다"
msg["From"] = EMAIL_ADDRESS
msg["To"] = "yuhyewon91@gmail.com"
msg.set_content("다운로드 하세요")

# 첨부파일 등록 : 파일을 읽어서 줘야함
# r: read text, rb: read img
# MIME 타입에 따라 maintype과 subtype이 다름
# MIME 타입 중 이미지 타입
with open("btn_brush.png", "rb") as f:
    msg.add_attachment(f.read(), maintype="image", subtype="png", filename=f.name)

with open("테스트.pdf", "rb") as f:
    msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=f.name)

with open("엑셀.xlsx", "rb") as f:
    msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename=f.name)

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)