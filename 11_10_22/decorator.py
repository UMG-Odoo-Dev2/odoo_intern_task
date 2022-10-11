def hello_decorator(func): # defining a decorator
    
    def inner1(): # Inner nested function 
        print("Hello, this is before function execution") 
    
        func() # Calling the actual function
    
        print("This is after function execution") 
            
    return inner1 
    
def function_to_be_used(): # Defining a function, to be called inside wrapper
    print("This is inside the function !!") 

function_to_be_used = hello_decorator(function_to_be_used) # Passing 'function_to_be_used' inside the decorator
    
function_to_be_used() # Calling the function 