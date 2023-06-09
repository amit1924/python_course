class Shape:
    def __init__(self,len,wd):
        self.length = len
        self.width = wd
        
        
    def area(self):
        return self.length*self.width    
    
class Circle(Shape):
        def __init__(self,radius):
            self.radius = radius
            super().__init__(radius,radius)
            
        def area(self):
            return 3.14 * super().area()    
    
    
# rec = Shape(100,100)
# print (rec.area())    


c =Circle(10)
print(c.area())