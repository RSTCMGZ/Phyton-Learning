#  #! set

# # liste = ['Mehmet', 'Ahmet', 'Mehmet', 'Hasan', 'Hasan', 'Mehmet', 'Ahmet']

# # tekrarsiz = set(liste)

# # print(tekrarsiz)

# kume1 = {'Mehmet', 'Hasan', 'Taner'}
# kume2 = {'Taner', 'Hasan', 'Mehmet Can', 'Yasemin'}


# kume3 = kume1.intersection(kume2) #kesişim
# # kume3 = kume1.union(kume2)

# print(kume3)

cift = {0,2,4,6,8}
tek = {1,3,5,7,9}
asal = {2,3,5,7}


print(cift.union(tek))
print(cift.intersection(asal))