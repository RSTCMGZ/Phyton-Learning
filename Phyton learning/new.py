sinif = [
{
'isim':'Mehmet',
'soyisim':'Çalışkan',
'cinsiyet':'Erkek',
'yaş':28,
'hobileri': ['Mağaracılık','Kamp','Fotoğrafçılık'],
'medeniHal':'Bekar',
'meslek':'Yazılımcı'

},
{
'isim':'Övünç',
'soyisim':'Türker',
'cinsiyet':'Erkek',
'yaş':29,
'hobileri':['MMORPG','Youtube Podcast','Ekşide Yazı Okumak'],
'medeniHal':'Bekar',
'meslek':'Renderci'
},
{
"isim":"Hasan",
"soyisim":"Akoluk",
"cinsiyet":"Erkek",
"yaş":31,
"hobileri": ["kitap okumak","spor yapmak"],
"medeniHal":"Bekar",
"meslek":"Yazılımcı"
},
{

'isim':'Reşat',
'soyisim':'Çamgöz',
'cinsiyet':'Erkek',
'yaş':28,
'hobileri':['Kitap okumak', 'kod yazmak', 'el işi yapmak', 'oyun oynamak'],
'medeniHal': 'Bekar',
'meslek':'Öğrenci'
},
{
"isim":"Utku",
"soyisim":"Şen",
"cinsiyet":"Erkek",
"yaş":27,
"hobileri":["Calisthenics","Kamp","Yüzme","Video Oyunları"],
"medeniHal":"Bekar",
"meslek":"Öğrenci"
},
{
'isim': 'Furkan',
'soyisim': 'Sevilmiş',
'cinsiyet' : 'Erkek',
'yaş' : 21,
'hobileri' : ['Bilgisayar oyunu oynamak','Kod yazmak','Fitness'],
'medeniHal': 'Bekar',
'meslek': 'Öğrenci',
},
{
'isim':'Engin Can' ,
'soyisim':'Türkoğlu',
'cinsiyet':'Erkek',
'yaş':22,
'hobileri':['Bilgisayar oyunu oynamak','Kod yazmak','Fitness'],
'medeniHal': 'Bekar',
'meslek': 'Öğrenci',
},
{
'isim':'Sonay',
'soyisim':'Topaloğlu',
'cinsiyet':'Kadın',
'yaş': 21,
'hobileri': ['yürüyüş','kitap okumak','yemek yapmak'],
'medenihali': 'bekar',
'meslek': 'öğrenci'
},
{
'isim':'Taner',
'soyisim':'Şaşmaz ',
'cinsiyet':'Erkek',
'yaş':32,
'hobileri': ['İtalya','Müzik','İnsanlık Tarihi'],
'medeniHal':'Evli',
'meslek':'Grafiker'
},
{
'isim': 'ömer',
'soyisim':'yılmaz',
'cinsiyet': 'erkek',
'yaş':32,
'hobileri':['mağaracılık','kamp','Fotoğrafcılık'],
'medenihal':'Evli',
'meslek': 'kursiyer'
},
{
'isim':'Mehmet Can',
'soyisim':'Güzel',
'cinsiyet':'Erkek',
'yaş':23,
'hobileri': ['Kamp','köpek eğitimi','okçuluk'],
'medeniHal': 'Bekar',
'meslek':'Serbest meslek'
},
{
"isim":"Serap",
"Soyisim":"Kaya",
"cinsiyet":"Kadın",
"yaş":32,
"hobileri": ["kitap okumak","resim yapmak "],
"medeniHal":"Bekar",
"meslek":"Sigortacı"
},
{
"isim":"Gürcan",
"soyisim":"ÇARIK",
"cinsiyet":"Belirtmek istemiyor Kvkk",
"yaş":22,
"hobileri":["Silah atış" , "Bilardo", "araba sürmek" ,"satranç","at binme"],
"medeni hali":"Evli",
"meslek":"Cloud Bilişim Siber Güvenliği"
},
{
'isim':'Yasemin',
'soyisim':'Şahbaz',
'cinsiyet':'Kadın',
'yaş' : 37,
'hobileri' : ['Doğa yürüyüşü', 'Kitap okumak', 'Yemek yapmak'],
'medeniHal': 'Bekar',
'meslek' :'Müşteri temsilcisi',
},
{
"isim":"Levent",
"soyisim":"Hotaman",
"cinsiyet":"Erkek",
"yaş":22,
"hobileri":["Film izlemek","Uyumak"],
"medeniHal":"Bekar",
"meslek":"Yazılımcı",
}
]

# kadınlar = []
# for i in sinif:
#     if i.get('cinsiyet') == 'Kadın':
#         kadınlar.append(i['isim'])
# print(kadınlar)

# for i in sinif:
#     i['yaş'] += 1
# print(sinif)

# for i in sinif:
#     i['Kurum'] = 'Neos'
# print(sinif)
# yas = 0
# enyasli = {}

# for i in sinif:
#     if yas < i['yaş']:
#         yas = i['yaş']
#         enyasli = i

# yas = enyasli['yaş']
# enGenc = {}
# for i in sinif:
#     if yas > i['yaş']:
#         yas = i['yaş']
#         enGenc = i

# print(enGenc)
# enGencileYaşıt = []
# for i in sinif:
#     if enGenc['yaş'] == i['yaş']:
#         enGencileYaşıt.append(i)

# print(len(enGencileYaşıt))
# kampcılar = []

# for i in sinif:
#     for l in i['hobileri']:
#         if l.casefold() == 'kamp':
#             kampcılar.append(i)

#     # if i['hobileri'].__contains__('kamp') or i['hobileri'].__contains__('Kamp'):
# print(kampcılar)

topluluk = ('Mehmet', 'Ahmet', 'Hüseyin', 'Cabbar') # =>tupple
#topluluk = 'Mehmet', 'Ahmet', 'Hüseyin', 'Cabbar' # =>böyle de kullanılır.


sinif_list = list(topluluk)

sinif_list.pop()

# print(sinif_list)

topluluk = tuple(sinif_list)

# print(topluluk[1])

deneme = 'Reşo', # tupple tek elemanlı olabilir fakat ',' koyulmalıdır.




