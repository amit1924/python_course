class Employee:
    
    def __init__(self,n,salary):
        self.name = n
        self.salary =salary

        
        
    def showDetails(self):
        print(f" i am {self.name} and my salary is {self.salary} ")    
    
    
    @classmethod
    def fromStr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1]) 
    
e = Employee("Abhishek",250000)
print(e.name)
print(e.salary)


        
string = "Amit-12000"        
# e1 =Employee(string.split("-")[0],string.split("-")[1])
e1 =Employee.fromStr(string)
print(e1.name)
print(e1.salary)

            
        