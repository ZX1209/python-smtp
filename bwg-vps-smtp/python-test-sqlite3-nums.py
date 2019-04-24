import sqlite3

connect = sqlite3.connect('quotescom')
cursor = connect.cursor()

cursor.execute('select ID from QUOTES order by ID DESC')
# cursor.execute('select count(*) from QUOTES ')

num = cursor.fetchone()[0]

connect.close()
print(num)