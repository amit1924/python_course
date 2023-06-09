class Person:
    def __init__(self ,name,age):
        self.name = name
        self.age = age
        
    
    def info(self):
            print(f"{self.name} is {self.age} years old")
        
        
person1 = Person("Amit",30)
print(person1.name)   
print(person1.age)

person1.info()


person2 = Person("Rashmi",28)
print(person2.name)

person2.info()

        