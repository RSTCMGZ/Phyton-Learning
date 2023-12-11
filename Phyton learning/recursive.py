#! recursive
#! faktoriyel hesaplama
# def faktoriyel(x):
#     sonuc = 1
#     if x == 1:
#         return sonuc
#     else:
#        return  x* faktoriyel(x-1)

# print(faktoriyel(5))
#! 0-100 arası topla
# def topla(x):
#     if x == 0:
#         return x
#     else:
#         return x + topla(x + 1)
    
# print(topla(100))
#! 100'e kadar olan cift sayıları topla

# def ciftTopla(x):
#     if x == 0:
#         return x
#     else:
#         if x % 2 == 0:
#             return x + ciftTopla(x-2)
#         else:
#              return x
    
# print(ciftTopla(100))
#! args ve kwargs tanımı

# def deneme(*args, **kwargs):
#     print(args)
#     print(kwargs)

# deneme('Reşo', 'Reşooo', 28, ['Merhaba'], {'isim': 'Reşo'},29,300,'asasdsad',(2,3,4), isim= 'Reşo')
 #! args ile toplama yaptık.
# def topla(*args, **kwargs):
#     toplam = 0
#     for i in args:
#         toplam += i
#     return toplam

# print(
# topla(5,25,10,69,58,48,79,52,19,65, sayı = 456, sayı2=500)
# )
 #! sum = toplar
# dizi = [10,300,420,45,77,98]

# print(sum(dizi))
#! Mukemmel sayi
# def mukemmel(x):
#     dizi = []
#     for i in range(1,x):
#         if x % i == 0:
#             dizi.append(i)
#             if sum(dizi) == x:
#                  return (f'mükemmel sayi {x}')
#             else:
#                 return print('degil')     


# for i in range(1,100):
#     print(mukemmel(i))
# #! Ebob  
# def ebob(x,y):
#     xBolenler = []
#     yBolenler = []
    
#     for i in range(1,x+1):
#         if x%i == 0:
#             xBolenler.append(i)
#     for i in range(1,y+1):
#         if x%i == 0:
#             yBolenler.append(i)       
#     deneme = list(set(xBolenler).intersection(set(yBolenler)))

#     return deneme[-1]

# ebob(5,15)
# #! Ekok
# def ekok(x,y):
#     xKatları = []
#     yKatları = []
#     for i in range(1,x*y):
#         xKatları.append(x*i)
#         yKatları.append(y*i)

#     ortak = set(xKatları).intersection(set(yKatları))    
#     ortakliste = list(ortak)
#     ortakliste.sort(reverse=False)
#     return ortakliste[0]

# print(
#     ekok(8,12)
# )
#! buyuk unlu uyumu

# def buyukUnlu(x):
#     kalın = ['a','ı','o', 'u']
#     ince = ['e','i','ö', 'ü']
#     liste = x.split(' ')
#     kelime = ''
#     kalın = 0
#     aı=0
#     ei=0
#     for i in liste:
#         for l in i.lower():
#             if l in kalın or l in ince:
#                 kelime += l
#     for i in kelime:
#         if i in kalın:
#             aı += 1
#         else:
#             ei +=1
#     if ei > 0 and aı >0:
#         return 'uymuyor'
#     else:
#         return'uyuyor'



# print(
# buyukUnlu('Merhaba')
# )
#! anagram kelime


# def anagram(x):
#     if x[::-1].lower() == x.lower():
#         return True
#     else:
#         return False
    
# print(
#     anagram('lale')
# )

#! dizi içindeki tekrarları al ve topla 

# def repeat_sum(l):
#     birlesim = []
#     tekrarlar = []

#     for i in l:
#         for x in set(i):
#             if x not in birlesim:
#                 birlesim.append(x)
#             else:
#                 if x not in tekrarlar:
#                     tekrarlar.append(x)
#     print(tekrarlar)
#     return sum(tekrarlar)


# print(
# repeat_sum([(1,2,3),(2,8,9),(7,123,8)])
# )


