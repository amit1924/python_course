class person:
    name = "Amit"
    age =30
    job ="python Developer"
    
    def info(self):  ## this ia a method(function)
        print(f"{self.name} is a {self.job}") ## self is an object(person1)
   
   
person1 =  person()   
person1.name = "Rashmi"
print(person1.age)
print(person1.name)
print(person1.job)

person1.info()

person2 = person()
person2.age = 32
print(person2.age)

person2.info() ## info is a method which is used to call peson2 object