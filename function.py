# # # # # # # def function_name(parameters):
# # # # # # #   pass
# # # # # # #   Code and Statements

# # # # # #     Create a function using the def keyword, followed by a function name, followed by a paranthesis (()) and a colon(:).
# # # # # #     Any parameters and arguments should be placed within the parentheses.
# # # # # #     Rules to naming function are similar to that of naming variables.
# # # # # #     Any statements and other code within the function should be indented.


# # # # # # def mul(a,b):
# # # # # #     print("The muliplication of a & b is: " , a*b)

# # # # # # mul(5,6)    

# # # # # def calculateGmean(a, b):
# # # # #   mean = (a*b)/(a+b)
# # # # #   print(mean)

# # # # # def isGreater(a, b):
# # # # #   if(a>b):
# # # # #     print("First number is greater")
# # # # #   else:
# # # # #     print("Second number is greater or equal")

# # # # # def isLesser(a, b):
# # # # #   pass  # pass means i am not executing now 
  

# # # # # a = 9
# # # # # b = 8
# # # # # isGreater(a, b)
# # # # # calculateGmean(a, b)
# # # # # # gmean1 = (a*b)/(a+b)
# # # # # # print(gmean1)
# # # # # c = 8
# # # # # d = 74
# # # # # isGreater(c, d)
# # # # # calculateGmean(c, d)
# # # # # # gmean2 = (c*d)/(c+d)
# # # # # # print(gmean2)




# # # # # default arguments
# # # # def name(fname, mname = "Jhon", lname = "Whatson"):
# # # #     print("Hello,", fname, mname, lname)

# # # # name("Amy")

# # # #Keyword arguments:
# # # def name(fname, mname, lname):
# # #     print("Hello,", fname, mname, lname)

# # # name(mname = "Peter", lname = "Wesker", fname = "Jade")

# # #Required arguments:

# # def name(fname, mname, lname):
# #     print("Hello,", fname, mname, lname)

# # name("Peter", "Quill", Alter)

# #Arbitrary Arguments:
# def name(*name):
#     print(type(name))
#     print("Hello,", name[0], name[1], name[2])

# name("James", "Buchanan", "Barnes")


# Return arguments

def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

# print(name("James", "Buchanan", "Barnes"))
c = name("James","Buchanan","Barnes")
print(c)