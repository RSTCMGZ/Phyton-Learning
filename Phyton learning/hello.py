# print("Hello World!")


# #! String
# name = "Reşo"
# number = "20"
# name_surname = "Reşat Çamgöz"
# #! integer
# num = 20
# #! Float
# number = 20.5
# #! Boolean
# true = True
# false = False
# #! List
# class_list = list(["Mehmet", "Ahmet"])
# class1 = ["Mehmet", "Ahmet", "Hüseyin", "Cabbar"]
# print(class1[0:3:2]) #?start-end increase amount
# print(class1[::-1])  #?start-end increase amount
# #! Object (dict)
# person =  {
#     "name" : "Reşo",
#     "age" : 28,
# }
# person1 = dict(
#     name= "Reso",
#     surname = "Cmgz",
# )

# #! tuple (non-modifiable list)

# class2 = ("Mehmet", "Ahmet", "Hüseyin", "Cabbar")
# class3 = "Mehmet", "Ahmet", "Hüseyin", "Cabbar"
# class4 = tuple("Mehmet",)

# print(type(number))

# #! set

# numbers = {1,2,3,4,5,6,7,1,2,4,5,7}
# numbers2 = {1,2,3,4,5,6,7,1,2,4,5,7}

# print(numbers)

# what_name = input("What is your name?")

# print(f"{what_name} welcome")
#! str to int
# number1 = input("Number1 enter: ")
# number2 = input("Number2 enter: ")

# print(int(f"{number1}") + int(f"{number2}"))
#! int to str
# number = 10

# print(type(number))

name = "reşo"

print(dir(name))

# print(name.capitalize())
# print(name.center(20,"a"))

# print(name.count("m")) # m have?
#print(name.endswith("m")) # start m ?
#print(name.startswith("m")) # finish m ?

#print(name.find("e")) 
# print(name.index("h"))
# print(name.islower())
# print(name.join())
# print(name.replace())
#print(name.split()) # string => string splits the expression and makes a list
#print(name.title())
#print(name.upper())
#print(name.lower())
#!comparison operators
# print(1<3)
# print(1>3)
# print(1 >=3)
# print(1 <= 3)
# print(1 == 3)
# print(1 == "1")
# print(1 != 1)
#!logical operators
#?and
# print(1<3 and 3< 2)
#?or
# print(1<3 or 3< 2)
#! if-else

name = "Reşo"

name_enter = input("Enter name")

if name.casefold() ==name_enter.casefold():
    print("successful")
elif name_enter == "ahmet":
    print("Ahmet")
else:
    print("not successful")

#! variables
