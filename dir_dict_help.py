class Employee:
    companyName = "Apple" # class variable(its defined under the class )
    def __init__(self,n,age):
        self.name = n
        self.age = age
        
        
e =Employee("amit",30)
print(e.__dict__)        