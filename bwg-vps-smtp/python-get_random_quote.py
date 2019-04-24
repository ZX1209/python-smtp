import sqlite3
import random

def getRandomQuote():
    connect = sqlite3.connect('quotescom')
    cursor = connect.cursor()
    rint = (random.randint(1,190),)
    cursor.execute('select QUOTE from QUOTES  where id = ?',rint)
    html = cursor.fetchone();
    connect.close()

    html = html[0]
    return html

if __name__ == '__main__':
    print(getRandomQuote())

