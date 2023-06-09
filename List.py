# # l = [ 2,4,6]
# # print(l[1])
# # print(type(l))

# # # colors = ["Red", "Green", "Blue", "Yellow", "Green"]
# # # if "Yellow" in colors:
# # #     print("Yellow is present.")
# # # else:
# # #     print("Yellow is absent.")

# animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[::2])		#using positive indexes
# print(animals[-8:-1:2])	#using negative indexes

lst = [i for i in range(4)]
print(lst)
lst = [i for i in range(10) if i%2==0]
print(lst)
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)