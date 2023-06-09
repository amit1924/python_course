class Employee:
   def __init__(self,n,age):
        self.name = n
        self.age = age
        
        
   def showDetails(self):
        print(f"{self.name} i am {self.age} years old")    
        
        
class Programmer(Employee):
    def showLanguages(self):
        print("the default language is python")     
        
        
        
e1 =Employee("amit",30)
print(e1.showDetails())    

e2 =Programmer("python" ,32)
print(e2.showLanguages())      