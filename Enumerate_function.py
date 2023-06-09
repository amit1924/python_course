# a = [12,56,32,98,100,12,45,1,4]

# index = 0
# for marks in a:
#     print(marks)

#     if(index==3):
#      print("Amit")
   
#     index = index+1

a = [12,56,32,98,100,12,45,1,4]

for index, marks in enumerate(a):
    print(marks)

    if(index==3):
     print("Amit")
    index = index+1 
   

fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(f'{index+1}: {fruit}')
