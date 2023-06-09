class Employee:
    companyName = "Apple" 
    def __len__(self):
        i=0
        for c in self.companyName:
            i = i+1
        return i    
            
        
        
        
e1 =Employee()
print(len(e1))
