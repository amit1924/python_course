class Math:
    def __init__(self,num):
        self.num =num
        
        
    def addtonum(self,n):
        self.num = self.num + n
        
        
    @staticmethod ## we use static method to not using self 
    def add(a,b):
        return a + b
    
    
    
a = Math(100)
print(a.num)        

a.addtonum(200)
print(a.num)        


print(a.add(5,6))
