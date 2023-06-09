# decorator is a function that takes another function as an argument and returns a new function that modified an original function

def greet (fx): ## greet is a decorator function
    def mfx():  ## modified function
        print("good morning")
        fx()
        print("good")
    return mfx  
   
    
    
    
    

    
@greet
def hello():     
    print ("hello world")    
    
# greet(hello)()
        
hello()    