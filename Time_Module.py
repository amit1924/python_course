import time

# # # a = time.gmtime()
# # # print(a)
# # # b = curr = time.time()
# # # print(b)


# # curr = time.ctime(1627908313.717886)
# # print("Current time:", curr)

# timestamp = time.strftime('%H,%M,%S')
# print(timestamp)

a = int(time.strftime('%H'))
if(a<12):
    print("good morning")
elif(12<a<18):
    print("good evening")


else:
    print("good night")



