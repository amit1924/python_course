# tup = (1, 2, 76, 342, 32, "green", True)
# # tup[0] = 90 #tupple object does not support item assignment
# print(type(tup), tup)
# print(len(tup))
# print(tup[0])
# print(tup[-1])
# print(tup[2])
# # print(tup[34])

# country = ("Spain", "Italy", "India",)
# #            [0]      [1]      [2]     
# print(country[0])
# print(country[1])
# print(country[2])

# country = ("Spain", "Italy", "India", "England", "Germany")
# if "Germany" in country:
#     print("Germany is present.")
# else:
#     print("Germany is absent.")

# animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
# print(animals[3:7])     #using positive indexes
# print(animals[-7:-2])   #using negative indexes

# animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
# print(animals[::2])     #using positive indexes
# print(animals[-8:-1:2]) #using negative indexes

# Operations in Tuples

# countries = ("Spain", "Italy", "India", "England", "Germany")
# temp = list(countries)
# temp.append("Russia")       #add item 
# temp.pop(3)                 #remove item
# temp[2] = "Finland"         #change item
# countries = tuple(temp)
# print(countries)

Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
# res = Tuple1.count(3)
res = Tuple1.index(3,4,8)
print('Count of 3 in Tuple1 is:', res)