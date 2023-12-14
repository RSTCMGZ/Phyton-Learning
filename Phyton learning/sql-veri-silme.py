import sqlite3

def isme_gore_sil(isim,yas):
    con = sqlite3.connect('giris.db')
    cur = con.cursor()

    remove_commit = f'DELETE FROM STUDENTS WHERE name ="{isim}" AND age = {yas}'
    # remove_commit = f'DELETE FROM STUDENTS ' tüm database'i siler.
    cur.execute(remove_commit)



    con.commit()
    con.close()

isme_gore_sil('Reşat', 22)

