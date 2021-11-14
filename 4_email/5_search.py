from imap_tools import MailBox # Search imap tools and study query
from account import *

# mailbox = MailBox("imap.gmail.com", 993)
# mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")
# mailbox.logout()

# Easier way with one line
with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    # 1. all mail
    # for msg in mailbox.fetch() : 
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 2. Get unread mails / '(UNSEEN)' : query
    # for msg in mailbox.fetch('(UNSEEN)'): 
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 3. Email from a specific person
    # for msg in mailbox.fetch('(FROM yuhyewon91@gmail.com)', limit=3): 
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 4. Mails containing certain letters (Title & Body)
    # Because it is imported through query, " and ' must be written equally.
    # Imported mail containing "test" and "mail"
    # for msg in mailbox.fetch('(TEXT "test mail")'): 
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 5. Mails containing certain letters(only en) in the title.
    # for msg in mailbox.fetch('(SUBJECT "test mail")'): 
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 5-2. Filtering Mails containing certain letters(ko) in the title.
    # for msg in mailbox.fetch(limit=5, reverse=True):
    #     if "테스트" in msg.subject:
    #         print("[{}] {}".format(msg.from_, msg.subject))

    # 6. Mails after a specific date / Refer to strftime.py
    # for msg in mailbox.fetch('(SENTSINCE 07-Nov-2020)', limit=5): 
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 6-1. Emails that came on a specific date.
    for msg in mailbox.fetch('(ON 07-Nov-2020)'): 
        print("[{}] {}".format(msg.from_, msg.subject))


    # 7. emails that satisfy two or more conditions.
    for msg in mailbox.fetch('(ON 07-Nov-2020 SUBJECT "test mail")'): 
        print("[{}] {}".format(msg.from_, msg.subject))

    # 7-1. emails that satisfy one of two or more conditions.
    for msg in mailbox.fetch('(OR ON 07-Nov-2020 SUBJECT "test mail")'): 
        print("[{}] {}".format(msg.from_, msg.subject))
