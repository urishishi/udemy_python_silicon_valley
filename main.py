import logging
import logging.handlers
# from email import message
import configparser
import smtplib
from email.mime import text
from email.mime import multipart


config = configparser.ConfigParser()
config.read("./config.ini")
# config_ini = configparser.ConfigParser()
# config_ini.read("config.ini", encoding="utf-8")

smtp_host = "smtp.gmail.com"
smtp_port = 587
from_email = "atsuhito.yamaoka@datumstudio.jp"
to_email = "atsuhito.yamaoka@supership.jp"
user = config["user"]["user"]
password = config["user"]["password"]

# msg = message.EmailMessage()
msg = multipart.MIMEMultipart()
# msg.set_content("test email")
msg["Subject"] = "test email subject"
msg["From"] = from_email
msg["To"] = to_email
msg.attach(text.MIMEText("test email", "plain"))

with open("./main.py", "r") as f:
    attachment = text.MIMEText(f.read(), "plain")
    attachment.add_header("Content-Disposition", "attachment", filename="main.py")
    msg.attach(attachment)

server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(user, password)
server.send_message(msg)
server.quit()
