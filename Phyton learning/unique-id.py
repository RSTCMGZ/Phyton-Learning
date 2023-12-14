import sqlite3

con = sqlite3.connect('yeni.db')
cur = con.cursor()

cur.execute('INSERT INTO OGRENCİ (ad,surname) VALUES ("Deneme", "Camgoz")')


con.commit()
con.close()