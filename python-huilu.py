import requests

from bs4 import BeautifulSoup


html = requests.get('https://www.huilv.cc/USD_CNY/')
soup = BeautifulSoup(html.text,features="html.parser")

r = soup.select('span.back')

print(r[0].text)