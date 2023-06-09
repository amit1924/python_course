class Employee:
    companyName = "Apple" # class variable(its defined under the class )
    def __init__(self,n,age):
        self.name = n
        self.age = age
        
        
    def showDetails(self):
        print(f"{self.name} i am {self.age} years old and my company is {self.companyName}")    
        
        
        
        
        
e1 =Employee("amit",30)
e1.companyName = "samsung" ## instance variable (it can change the class variable value)

Employee.showDetails(e1)   
e1.showDetails()       

e2 = Employee("Abhishek",32)
e2.showDetails() 