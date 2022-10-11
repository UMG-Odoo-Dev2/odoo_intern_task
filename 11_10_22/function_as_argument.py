def makeUpper(text): # a function for making text upper
    return text.upper() 
    
def makeLower(text): # a function for making text lower
    return text.lower() 
    
def greet(func): # A third function that work as a high order function
     
    greeting = func("Hello, How are you?") # Storing the function in a variable in high order function 
    print(greeting)  
    
greet(makeUpper) 
greet(makeLower)