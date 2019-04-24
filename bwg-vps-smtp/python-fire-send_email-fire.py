#!/usr/bin/python3
# -*- coding: utf-8 -*-
import fire
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# mailto:list[str]


def sendEmail(title="nothing", detail="as the subject", format='plain', mailto=['1404919041@qq.com'],
              mailfrom='my-bwg-vps'):
    if type(mailto) is str:
        mailto = [mailto]

    # message = MIMEText(detail, format, 'utf-8')
    # message['From'] = Header(mailfrom, 'utf-8')
    # message['To'] = Header(",".join(mailto), 'utf-8')
    # message['Subject'] = Header(title, 'utf-8')

    message = MIMEText(detail, format, 'utf-8')
    message['From'] = mailfrom
    message['To'] = ",".join(mailto)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(mailfrom, mailto, message.as_string())
        smtpObj.quit()
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")

if __name__ == '__main__':
    fire.Fire()
