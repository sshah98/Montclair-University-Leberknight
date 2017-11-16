import smtplib
import socks
import openpyxl, sys
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

gmail_user = ""
gmail_pwd = ""

def mail(to, subject, text, attach):
    
    
    # socks.setdefaultproxy(TYPE, ADDR, PORT)
    # socks.setdefaultproxy(socks.SOCKS5, 'http://191.252.100.170', 80)
    # socks.wrapmodule(smtplib)
    
    socks.setdefaultproxy(socks.SOCKS5, '201.148.127.58', 3128)
    socks.wrapmodule(smtplib)
    
    msg = MIMEMultipart()
    
    msg['From'] = gmail_user
    msg['To'] = to
    msg['Subject'] = subject
    
    msg.attach(MIMEText(text))
    
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(attach, 'rb').read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition',
    'attachment; filename="%s"' % os.path.basename(attach))
    msg.attach(part)
    
    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd)
    mailServer.sendmail(gmail_user, to, msg.as_string())
    # Should be mailServer.quit(), but that crashes...
    mailServer.close()
    
mail("shahsuraj261@gmail.com", "Hello from python!", "This is a email sent with python", "good-proxies.txt")
    
    