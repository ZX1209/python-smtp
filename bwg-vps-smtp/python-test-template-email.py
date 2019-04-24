#!/usr/bin/python3
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from string import Template

# mailto:list[str]


def sendEmail(title="nothing", detail="as the subject", format='plain', mailto=['1404919041@qq.com'],
              mailfrom='my-bwg-vps'):
    """
    title:str
    detail:str
    format:special str
    mailto:list[str]
    mailfrom:str
    """
    if type(mailto) is str:
        mailto = [mailto]

    # 生成邮件信息
    # message = MIMEText(detail, format, 'utf-8')
    # message['From'] = Header(mailfrom, 'utf-8')
    # message['To'] = Header(",".join(mailto), 'utf-8')
    # message['Subject'] = Header(title, 'utf-8')

    message = MIMEText(detail, format, 'utf-8')
    message['From'] = mailfrom
    message['To'] = ",".join(mailto)
    message['Subject'] = Header(title, 'utf-8')

    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(mailfrom, mailto, message.as_string())
        smtpObj.quit()
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


if __name__ == '__main__':

    quoteTemplate = """
    <body style="margin-bottom: 60px;">
    <div class="quote" style="padding: 10px;margin-bottom: 30px;border: 1px solid #333333;border-radius: 5px;box-shadow: 2px 2px 3px #333333;"itemscope="" itemtype="http://schema.org/CreativeWork">
    <span class="text" itemprop="text">
    $quote
    </span>
    <br />
    <span>by 
    <small class="author" style="font-weight: bold;color: #3677E8;"itemprop="author">
    $author
    </small>
    </span>
    </div>
    </body>
    """

    s = Template(quoteTemplate)
    ts = s.substitute(quote='test quote',author='test author')


    sendEmail(title='template test',detail=ts,format='html',mailto=['1404919041@qq.com','zxgaoling@gmail.com'])


