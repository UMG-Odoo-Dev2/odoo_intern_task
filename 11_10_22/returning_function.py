def create_adder(x): # A function for addition 
    def adder(y): # Nested function with second number 
        return x + y # Addition of two numbers
    
    return adder  # Result
    
add_15 = create_adder(15) # Assigning nested adding function to a variable 
    
print(add_15(10)) # Using variable as high order function 