sehirler=["Adana", "Adıyaman", "Afyon", "Ağrı", "Amasya", "Ankara", "Antalya", "Artvin", "Aydın", "Balıkesir", "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkari", "Hatay", "Isparta", "Mersin", "İstanbul", "İzmir", "Kars", "Kastamonu", "Kayseri", "Kırklareli", "Kırşehir", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Kahramanmaraş", "Mardin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu", "Rize", "Sakarya", "Samsun", "Siirt", "Sinop", "Sivas", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Şanlıurfa", "Uşak", "Van", "Yozgat", "Zonguldak", "Aksaray", "Bayburt", "Karaman", "Kırıkkale", "Batman", "Şırnak", "Bartın", "Ardahan", "Iğdır", "Yalova", "Karabük", "Kilis", "Osmaniye", "Düzce"
]

print(dir(sehirler))

# sehirler.append('Torbalı') ekler
# sehirler.clear() hepsini siler
# sehirler.pop() #sondakini siler

# sehirler.remove('Yalova') yazdığını siler
#sehirler.pop(1) 1. diziyi seçer
# print(sehirler.count('Ad')) dizi içinde  aratır
#print(len(sehirler)) uzunlugunu yazar

#print(sehirler.index('içel'))
# sehirler.sort()
# sehirler.reverse()
# print(sehirler)

# number = [2,3,4,5,6,7,23,43,21,56,78,99]

# number.sort()
# number.reverse()
# print(number)

# sayılar = list(range(2,10))

# print(sayılar)
#! 0-100'e kadar çift sayılar
# sayilar = list(range(0,101,2)) #başlangıç,bitiş,artış-azalış
# print(sayilar)

#! FOR

# for i in sehirler:
#     print(i)
# a_ile_biten_sehirler = []
# b_ile_biten_sehirler = []
# for i in sehirler:
#     if i.endswith('a'):
#         a_ile_biten_sehirler.append(i)
#     if i.endswith('b'):
#         b_ile_biten_sehirler.append(i)
# if len(a_ile_biten_sehirler) > len(b_ile_biten_sehirler):
#     print('a')
# else:
#     print('b')

# en_uzun = ''

# for sehir in sehirler:
#     if len(en_uzun) < len(sehir):
#         en_uzun = sehir
    
# print(en_uzun)

# e = ''

# for i in sehirler:
#     if e.count('e') > i.count('e'):
#         e = i

# print(e)

