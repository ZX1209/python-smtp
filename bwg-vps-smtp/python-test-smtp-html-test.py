#!/usr/bin/python3
# -*- coding: utf-8 -*-

# import fire
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

html = """
<body style="margin-bottom: 60px;">
<div class="quote" style="padding: 10px;margin-bottom: 30px;border: 1px solid #333333;border-radius: 5px;box-shadow: 2px 2px 3px #333333;"itemscope="" itemtype="http://schema.org/CreativeWork">
<span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>
<span>by <small class="author" style="font-weight: bold;color: #3677E8;"itemprop="author">Albert Einstein</small>
<a href="/author/Albert-Einstein">(about)</a>
</span>
<div class="tags" style="margin-top: 10px;">
            Tags:
            <meta class="keywords" content="change,deep-thoughts,thinking,world" itemprop="keywords"/>
<a class="tag" type="padding: 2px 5px;
  border-radius: 5px;
  color: white;
  font-size: small;
  background-color: #7CA3E6;"href="/tag/change/page/1/">change</a>
<a class="tag" type="padding: 2px 5px;
  border-radius: 5px;
  color: white;
  font-size: small;
  background-color: #7CA3E6;"href="/tag/deep-thoughts/page/1/">deep-thoughts</a>
<a class="tag" type="padding: 2px 5px;
  border-radius: 5px;
  color: white;
  font-size: small;
  background-color: #7CA3E6;"href="/tag/thinking/page/1/">thinking</a>
<a class="tag" type="padding: 2px 5px;
  border-radius: 5px;
  color: white;
  font-size: small;
  background-color: #7CA3E6;"href="/tag/world/page/1/">world</a>
</div>
</div>
</body>
"""

sendEmail(title="smtp html 测试",detail=html,mailto=['zxgaoling@gmail.com','1404919041@qq.com'],format='html')
print(html)
# if __name__ == '__main__':
#     fire.Fire()
