import sqlite3

def adi_degistir(name):
    con = sqlite3.connect('giris.db')
    cur = con.cursor()

    # update_commit = f'UPDATE  STUDENTS  SET name="{newName}" WHERE name = "{oldName}"'

    update_commit = f'UPDATE STUDENTS SET age = age + 1 WHERE name ="{name}"'

    cur.execute(update_commit)

    con.commit()
    con.close()

# adi_degistir('Gürcan', 'Cabbar')
adi_degistir('Yasemin')