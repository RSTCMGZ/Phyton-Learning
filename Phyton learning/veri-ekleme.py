import sqlite3

# connect = sqlite3.connect('giris.db')
# cursor = connect.cursor()

# add_commit = 'INSERT INTO STUDENTS VALUES ("resooo","cmgzzzz",28)'

# add_commit = 'INSERT INTO STUDENTS VALUES {}'
# data = ('Reşat', 'ÇMGZ',28)
# cursor.execute(add_commit.format(data))


# connect.commit()
# connect.close()

def yeni_kisi_ekle(ad,soyad,yas):
    con = sqlite3.connect('giris.db')
    cur = con.cursor()

    add_commit = f'INSERT INTO STUDENTS VALUES ("{ad}","{soyad}",{yas})'

    cur.execute(add_commit)

    con.commit()
    con.close()

eklenecekler = [('Mehmet','Çalışkan',28),('Gürcan', 'Çarık',22),('Utku', 'Şen',27),('Serap','Kaya',32),('Yasemin','Şahbaz',37)]

def cokluEkle(liste):
    con = sqlite3.connect('giris.db')
    cur = con.cursor()
    for ad,soyad,yas in liste:
        add_commit = f'INSERT INTO STUDENTS VALUES ("{ad}","{soyad}",{yas})'
        cur.execute(add_commit)
        
    con.commit()
    con.close()

cokluEkle(eklenecekler)
