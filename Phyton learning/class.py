# # #! CLASS


# # class Person:
# #     kisi_sayisi = 0
# #     def __init__(self,isim,soyisim,cinsiyet,yas):
# #         self.name = isim
# #         self.surname = soyisim
# #         self.gender = cinsiyet
# #         self.age = yas
# #         self.mail = self.name + self.surname + "@sirket.com"
# #         Person.kisi_sayisi += 1



# #     def kendini_tanıt(self):
# #         return f'Benim adım {self.name} soyadım {self.surname}, {self.age} yaşındayım.'


# # class Yazilimci(Person):
# #     def __init__(self,isim,soyisim,cinsiyet,yas,bildigi_diller,sınıfları):
# #         super().__init__(isim,soyisim,cinsiyet,yas)

# #         self.lang = bildigi_diller 
# #         self.classes = sınıfları

# # egitim_dan1 = Person('Hatice','yyyy','Kadın',25)
# # egitim_dan2 = Person('Funda','yyyy','Kadın',25)

# # egitmen1 = Yazilimci('Reso', 'CMGZ', 'Eğitmen', 'Erkek', 28, ['HTML', 'CSS'], ['9 Ekim akşam'])

# # print(Person.kisi_sayisi)

# # # reso = Person('Reşo','CMGZ','Erkek',28)
# # # mehmet = Person('Mehmet','CMGZzzz','Erkek',28)
# # # print(reso.__dict__)
# # # print(reso.name)
# # # print(mehmet.kendini_tanıt())

# # # print(reso.kisi_sayisi)
# # # print(Person.kisi_sayisi)
# # # print(reso.id)
# # # print(mehmet.id)
# # # print(reso.mail)
# # # print(mehmet.mail)




# # class Quiz:
# #     dogru : 0
# #     def __init__(self,konu):
# #         self.konu = konu
# #         self.sorular = []
# #         self.sinavaGiren = ""
# #         self.mail = ""
# #     def soru_ekle(self,soru):
# #         return self.sorular.append(soru)
    
# #     def soruları_goster(self):
# #         for i in self.sorular:
# #             print(i.__str__())
    
# #     def sinava_basla(self):

# #         isim = input('Adiniz nedir')
# #         mail = input('Mail adresiniz  nedir')

# #         self.sinavaGiren = isim
# #         self.mail = mail
# #         soru_puani = 100 / (len(self.sorular))

# #         for i in self.sorular:
# #             print(i.soru)
# #             print(i.secenekler[0])
# #             cevap = input('Dogru cevap nedir?:')
# #             if cevap == i.dogruCevap:
# #                 Quiz.dogru += 1
# #         print(f'{isim}, {Quiz.dogru * soru_puani} puan aldin')
    
# #     def __str__(self):
# #         return f'Konu: {self.konu} Sorular {self.sorular}'

# # class Sorular:
# #     dogru = 0
# #     def __init__(self,soru,secenekler,dogruCevap):
# #         self.soru = soru
# #         self.secenekler = [secenekler]
# #         self.dogruCevap = dogruCevap
# #     def __str__(self):
# #         return f'Soru: {self.soru} Sorular {self.secenekler}, Dogru {self.dogruCevap}'

# # soru1 = Sorular('2 + 5 nedir', {'A) 3', 'B) 4', 'C) 6', 'D) 7'}, 'D')
# # soru2 = Sorular('2 + 2 nedir', {'A) 3', 'B) 4', 'C) 6', 'D) 7'}, 'B')
# # soru3 = Sorular('5 + 5 nedir', {'A) 10', 'B) 4', 'C) 6', 'D) 7'}, 'A')
# # soru4 = Sorular('3 + 3 nedir', {'A) 10', 'B) 4', 'C) 6', 'D) 7'}, 'C')

# # quiz1 = Quiz('Matematik')

# # quiz1.soru_ekle(soru1)
# # quiz1.soru_ekle(soru2)
# # quiz1.soru_ekle(soru3)
# # quiz1.soru_ekle(soru4)

# # quiz1.sinava_basla()
# #  ürün aldıgım ürün verdiğim ürünü üreten insanlar
# class insan:
#     def __init__(self,ad,soyad,tel,mail):
#         self.ad = ad
#         self.soyad = soyad
#         self.tel=tel
#         self.mail = mail

# class Tedarikci(insan):
#     def __init__(self, ad, soyad, tel,  mail, fatura_bilgisi = 'adresim' , urun = {}):
#         super().__init__(ad, soyad, tel, mail)
#         if urun != {}:
#             self.urun= [urun]
#         else:
#             self.urun = []
#         self.fatura_bilgisi = fatura_bilgisi
    
#     def urun_ekle(self,yeni_urun):
#         self.urun(yeni_urun)
#     def urun_cikar(self,cikarilacak_urun):
#         for i in self.urun:
#             if i.['Adi'] == cikarilacak_urun
#         print(cikarilacak_urun['adı'])

# class Musteri(insan):   
#     def __init__(self, ad, soyad, tel, mail,adres,bakiye):
#         super().__init__(ad, soyad, tel, mail)
#         self.adres = adres
#         self.bakiye = bakiye

# cocacola = Tedarikci('coca-cola', 'Coca-Cola company','5555555555', 'cocacola@gmail.com')

# cocacola.urun_ekle({'Adi':'Zero', 'Fiyat': '3Tl'})
# cocacola.urun_ekle({'Adi':'ice-tea', 'Fiyat': '4Tl'})

# print(cocacola.urun)