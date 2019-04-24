# sudo apt-get install sendmail
# sudo service sendmail start

# pip3 install bs4
# pip3 install requests

#!/usr/bin/python3
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def getHuilu():
    html = requests.get('https://www.huilv.cc/USD_CNY/')
    soup = BeautifulSoup(html.text,features="html.parser")

    r = soup.select('span.back')

    if r != []:
        return r[0].text
    else:
        return "error: nothing"
# mailto:list[str]


def sendEmail(subject="nothing", mess="as the subject", format='plain', mailto=['1404919041@qq.com'],
              mailfrom='myvps@vps.com'):

    # 生成邮件信息
    message = MIMEText(mess, format, 'utf-8')
    message['From'] = mailfrom
    message['To'] = ",".join(mailto)
    message['Subject'] = subject

    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(mailfrom, mailto, message.as_string())
        print("邮件发送成功")
    except:
        print("邮件发送失败")



hui = getHuilu()
dt = datetime.now().isoformat()
message = dt + " : " + hui
sendEmail(subject="每日汇率提醒",mess=message)