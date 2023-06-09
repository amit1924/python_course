class Employee:
    companyName = "Apple" # class variable(its defined under the class )
    def __init__(self,n):
        self.name = n

        
        
    def showDetails(self):
        print(f" i am {self.name} and my company is {self.companyName}")    
        
    @classmethod     
    def changeCompany(cls,newCompany):
        cls.companyName = newCompany
        
        
        
e1 =Employee("Amit")
e1.showDetails()
e1.changeCompany("Xiaomi")
e1.showDetails()
            
        