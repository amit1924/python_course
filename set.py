# Sets are unordered collection of data items. They store multiple items in a single variable. Set items are separated by commas and enclosed within curly brackets {}. Sets are unchangeable, meaning you cannot change items of the set once created. Sets do not contain duplicate items.

info = {"Carla", 19, False, 5.9, 19}
print(info) #Here we see that the items of set occur in random order and hence they cannot be accessed using index numbers. Also sets do not allow duplicate values.

# info = {"Carla", 19, False, 5.9}
# for item in info:
#     print(item)

a ={}
print(type(a))
a =set()
print(type(a))