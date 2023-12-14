import sqlite3

def goruntule():

    connect = sqlite3.connect('giris.db')
    cursor = connect.cursor()

    cursor.execute('SELECT * FROM STUDENTS WHERE age BETWEEN 25 and 30')
    all = cursor.fetchall()
    for i in all:
        print(i)
    connect.commit()
    connect.close()


goruntule()
