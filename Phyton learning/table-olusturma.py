import sqlite3

con = sqlite3.connect('giris.db')
cursor = con.cursor()


print('cursor olusturuldu')

cursor.execute('CREATE TABLE IF NOT EXISTS STUDENTS(name TEXT,lastname TEXT,age INT)')
con.commit()
con.close()