import sqlite3

def hesap_ac(name,surname,sifre):
    connect = sqlite3.connect('banka.db')
    cur = connect.cursor()

    add_commit = f'INSERT INTO MUSTERI (name,surname,bakiye,sifre) VALUES("{name}", "{surname}",0,{sifre})'

    cur.execute(add_commit)

    connect.commit()
    connect.close()


# name = input('Adiniz:')
# surname = input('Soyadiniz:')
# sifre = int(input('Sifre:'))

# hesap_ac(name,surname,sifre)

def kullanici_giris(isim,sifre):
        connect = sqlite3.connect('banka.db')
        cur = connect.cursor()

        cur.execute(f'SELECT * FROM MUSTERI WHERE name = "{isim}" AND sifre={sifre}')
        varmi = cur.fetchall()

        connect.commit()
        connect.close()

        if varmi == []:
            return False
        else:
            return True
def bakiye_sorgula(isim,sifre):
    connect = sqlite3.connect('banka.db')
    cur = connect.cursor()

    add_commit = f'INSERT INTO MUSTERI (name,surname,bakiye,sifre) name = "{isim}" AND sifre={sifre})'
    
    cur.execute(add_commit)

    connect.commit()
    connect.close()
    return varmi
while True:

    adiniz = input('Adiniz nedir?')
    sifreniz = int(input(' Dört haneli sifrenizi kodlayin:?'))
    if kullanici_giris(adiniz,sifreniz):
        neYapacaksın = input('Yapmak istediğiniz işlemi \n1-Bakiye Sorgula \n2-Para Çek \n3-Para Yatır \n4-Çıkış Yap')
        if neYapacaksın == '1':
            print(f'Mevcut bakiyeniz : {bakiye_sorgula(adiniz,sifreniz)}')
        elif neYapacaksın == '2':
             
    else:
         print('Kullanici adi veya sifre hatali')






