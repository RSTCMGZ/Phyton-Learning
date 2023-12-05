#! İF-ELSE EXAMPLES

# yas = int(input('Yasınız Kaç?'))
# arkadas = input('Arkadasin var mi ? (evet-hayir)')

# if yas < 18 and arkadas == 'evet':
#     print(f'Yasın kucuk {18-yas} yıl sonra gelebilirsin.')
# elif yas >= 18 and arkadas == 'hayir':
#     print('bir arkadas edinip mekana girebilirsin')
# elif yas < 18 and arkadas == 'hayir':
#     print('Hadi abicim kalabalik etme')
# else:
#     print('Mekana Hoşgeldin Ağabey')

#! öğrenciden 3 farklı not alın ve ortalama hesaplayın.Eğer 45 aldıysa vasat eğer 70 aldıysa iyi 100 aldıysa pek iyi deyin.

# not1 = int(input('birinci notu girin'))
# not2 = int(input('ikinci notu girin'))
# not3 = int(input('ücüncü notu girin'))

# ortalama = (not1 + not2+ not3)/3

# if ortalama <= 45:
#     print('Ortalama vasat')
# elif(ortalama <= 70):
#     print('Ortalama iyi')
# else:
#     print('ortalama pek iyi')

#! While
# i=0

# while i< 10:
#     print(i)
#     i+= 1
# else:
#     print(i)
# i = 0

# while i < 10:
#     i+= 1
#     if i == 5:
#         continue
#     print(i)

# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i+= 1
#! Tek mi çift mi sorusu ?
# sayi = int(input('Bir sayi giriniz'))

# if sayi % 2 == 0:
#     print('sayi cifttir')
# else:
#     print('sayi tektir')
#! 0-100 arası yazdır yanında çift ise çift tek ise tek yazsın.
# i = 0

# while i <= 100:
#     if i % 2 == 0:
#         print(f'{i}sayi cifttir')
#     else:
#         print(f'{i}sayi tektir')
#     i+=1
#! Random Sayi Üretme

# import random
# print(random.randint(0,10))
# import random
# print(random.randint(0,100))

# print(random.choice(['tas', 'kagıt', 'makas'])) #random select

# print(random.choices(['tas', 'kagıt', 'makas'], k=2))


#! Taş-Makas-Kağıt Oyunu
# import random
# beraberlik = 0
# kullanici = 0
# bilgisayar = 0
# while True:
#     kullanici_secimi = input('1- Kagıt \n2- Makas \n3- Tas')
#     bilgisayar_secimi = random.choice(['tas','kagıt','makas'])
    
#     if(kullanici_secimi == '1' and bilgisayar_secimi == 'kagıt') or (kullanici_secimi == '2' and bilgisayar_secimi == 'makas') or(kullanici_secimi == '3' and bilgisayar_secimi == 'tas'):
#         print(f'Beraberlik bilgisayar = {bilgisayar} kullanıcı = {kullanici}')
#         beraberlik += 1
#     elif(kullanici_secimi == '1' and bilgisayar_secimi == 'tas') or (kullanici_secimi == '2' and bilgisayar_secimi == 'kagıt') or(kullanici_secimi == '3' and bilgisayar_secimi == 'makas'):
#         kullanici += 1
#         print(f'Kazandınız bilgisayar = {bilgisayar} kullanıcı = {kullanici}')
#     else:
#         bilgisayar += 1
#         print(f'Kaybettiniz bilgisayar = {bilgisayar} kullanıcı = {kullanici}')
#     if bilgisayar + kullanici + beraberlik == 3:
#         if bilgisayar > kullanici:
#             print('bilgisayar kazandi')
#         elif bilgisayar < kullanici:
#             print(' kazandiniz')
#         else:
#             print('berabere kaldınız.')
#         break
#! Sayi Tahmin Oyunu
import random

rastgele_sayi = random.randint(0,10)
print(rastgele_sayi)
hak = 3
while True:
    kullanici_sayi = int(input('bir sayı tahmin ediniz (0-10)'))
    hak-=1
    if kullanici_sayi > rastgele_sayi:
        print(f'Daha kücük sayi girin {hak} hakkınız kaldı')
    elif kullanici_sayi < rastgele_sayi:
        print(f'Daha büyük sayı giriniz {hak} hakkınız kaldı')
    else:
        print(f'Tebrikler kazandınız {3 - hak} kere de bildin kaldı')
        break
    if hak == 0:
        print('kaybettiniz')
        break

    