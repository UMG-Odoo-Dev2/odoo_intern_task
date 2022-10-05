from multiprocessing.spawn import old_main_modules


class Example: 

    def __init__(self): 
        print("Example Instance.")
  
    def __del__(self): 
        print("Destructor called, Example deleted.") 
    
obj = Example() 
del obj
print(obj)

