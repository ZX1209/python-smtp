#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sqlite3
import logging as log
import random

import smtplib
from email.mime.text import MIMEText
from email.header import Header


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

connect = sqlite3.connect('quotescom')
cursor = connect.cursor()
rint = (random.randint(1,190),)
cursor.execute('select QUOTE from QUOTES  where id = ?',rint)
html = cursor.fetchone();
connect.close()

html = html[0]



sendEmail(title="your daily quotes",detail=html,mailto=['zxgaoling@gmail.com','1404919041@qq.com'],format='html')

# if __name__ == '__main__':
#     fire.Fire()
