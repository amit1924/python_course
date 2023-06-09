# info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info)
# info.update({'age':20})
# info.update({'DOB':2001})
# print(info)

# Clear
# info = {'name':'Karan', 'age':19, 'eligible':True}
# info.clear()
# print(info)

# POP
# info = {'name':'Karan', 'age':19, 'eligible':True}
# info.pop('eligible')
# print(info)

# Pop Item
# info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
# info.popitem()
# print(info)

# del (it's a keyword)
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)