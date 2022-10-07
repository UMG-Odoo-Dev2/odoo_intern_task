class Example: 
    
    # Initializing
    def __init__(self): 
        print("Example Instance.")
  
    # Calling destructor
    def __del__(self): 
        print("Destructor called, Example deleted.") 
    
obj = Example() 
del obj 
#print(obj)  #Will raise ERROR