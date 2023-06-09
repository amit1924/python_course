# # # l = [1,2,3,4,5,0,18,99,50]
# # # l.append(6)
# # # # l.sort()
# # # # l.sort(reverse=True)
# # # print(l.index(99))
# # # print(l)

# # colors = ["voilet", "green", "indigo", "blue"]
# # newlist = colors.copy()
# # newlist[0] ="indigo"
# # print(colors)
# # print(newlist)

# colors = ["voilet", "indigo", "blue"]
# #           [0]        [1]      [2]

# colors.insert(1, "green")   #inserts item at index 1
# # updated list: colors = ["voilet", "green", "indigo", "blue"]
# #       indexs              [0]       [1]       [2]      [3]

# print(colors)

#add a list to a list
# colors = ["voilet", "indigo", "blue"]
# rainbow = ["green", "yellow", "orange", "red"]
# colors.extend(rainbow)
# print(colors)

colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)