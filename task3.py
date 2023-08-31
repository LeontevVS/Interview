import os
import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from dotenv import load_dotenv

class Gmail:
    def __init__(self, login, password) -> None:
        load_dotenv()
        self.login = login
        self.password = password
        self.gmail_smtp = os.getenv('GMAIL_SMTP')
        self.gmail_port = os.getenv('GMAIL_PORT')
        self.gmail_imap = os.getenv('GMAIL_IMAP')
    
    def send(self, recipients, subject, message):
        to_email = ', '.join(recipients)
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        server = smtplib.SMTP(self.gmail_smtp, self.gmail_port)
        server.starttls()
        server.login(self.login, self.password)
        server.sendmail(self.login, to_email, msg.as_string())
        server.quit()

    def recieve(self, mailbox="inbox", header=None):
        mail = imaplib.IMAP4_SSL(self.gmail_imap)
        mail.login(self.login, self.password)
        mail.select(mailbox)
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()
        return email_message


if __name__ == '__main__':
    login = 'login@gmail.com'
    password = 'qwerty'
    mail = Gmail(login, password)
    recipients = ['vasya@email.com', 'petya@email.com']
    subject = 'Subject'
    message = 'Message'
    mail.send(recipients, subject, message)
    header = None
    mailbox = "inbox"
    mail.recieve(mailbox, header)