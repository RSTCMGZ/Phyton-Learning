#! CLASS


class Person:
    kisi_sayisi = 0
    def __init__(self,isim,soyisim,cinsiyet,yas):
        self.name = isim
        self.surname = soyisim
        self.gender = cinsiyet
        self.age = yas
        self.mail = self.name + self.surname + "@sirket.com"
        Person.kisi_sayisi += 1



    def kendini_tanıt(self):
        return f'Benim adım {self.name} soyadım {self.surname}, {self.age} yaşındayım.'


class Yazilimci(Person):
    def __init__(self,isim,soyisim,cinsiyet,yas,bildigi_diller,sınıfları):
        super().__init__(isim,soyisim,cinsiyet,yas)

        self.lang = bildigi_diller 
        self.classes = sınıfları

# reso = Person('Reşo','CMGZ','Erkek',28)
# mehmet = Person('Mehmet','CMGZzzz','Erkek',28)
# print(reso.__dict__)
# print(reso.name)
# print(mehmet.kendini_tanıt())

# print(reso.kisi_sayisi)
# print(Person.kisi_sayisi)
# print(reso.id)
# print(mehmet.id)
# print(reso.mail)
# print(mehmet.mail)

egitim_dan1 = Person('Hatice','yyyy','Kadın',25)
egitim_dan2 = Person('Funda','yyyy','Kadın',25)

egitmen1 = Yazilimci('Reso', 'CMGZ', 'Eğitmen', 'Erkek', 28, ['HTML', 'CSS'], ['9 Ekim akşam'])

print(Person.kisi_sayisi)

