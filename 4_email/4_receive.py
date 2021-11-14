from imap_tools import MailBox # $ pip install imap-tools
from account import *

mailbox = MailBox("imap.gmail.com", 993) # obj
mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") # INBOX : 받은 편지함

# fetch에 속성을 안주면 오래된 것부터 모두 가져옴
for msg in mailbox.fetch(limit=1, reverse=True):
    print("제목: ", msg.subject)
    print("발신자", msg.from_)
    print("수신자", msg.to)
    # print("참조자", msg.cc)
    # print("비밀참조자", msg.bcc)
    print("날짜", msg.date) # 20:19:41-08:00 means GMT-8. Ko is GMT+9. So 20(:19:41) + 19h is ko time
    print("본문", msg.text)
    print("HTML 메시지", msg.html)
    print("=" * 100)

    # Download attachments
    for att in msg.attachments:
        print("첨부파일 이름", att.filename)
        print("타입", att.content_type)
        print("크기", att.size)

        with open("download_" + att.filename, "wb") as f:
            f.write(att.payload)
            print("첨부 파일 {} 다운로드 완료".format(att.filename))

mailbox.logout()