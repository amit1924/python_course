def f1():


 try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
    


 except:
    print("Some error occurred")
    return 0

#  finally:
#     print("I am always Executed")
print("I am always Executed")

x = f1()
print(x)
