# Higher Order Functions in Python

A function that is having another function as an argument or a function that returns another function as a return in the output is called the High order function.

### Properties of higher-order functions:

- A function is an instance of the Object type.
- You can store the function in a variable.
- You can pass the function as a parameter to another function.
- You can return the function from a function.
- You can store them in data structures such as hash tables, lists, …
### Functions as objects

- A function can be assigned to a variable
~~~Python
def makeUpper(text): 
    return text.upper() 
    
print(makeUpper('Hello')) 
upperResult = makeUpper 
    
print(upperResult('Hello'))
~~~
In the above example, a function object referenced by makeUpper and creates a second name pointing to it, upperResult.

### Passing Function as an argument to other function

- Functions are like objects in Python, therefore, they can be passed as argument to other functions.

~~~Python
def makeUpper(text): 
    return text.upper() 
    
def makeLower(text): 
    return text.lower() 
    
def greet(func): 
     
    greeting = func("Hello, How are you?") 
    print(greeting)  
    
greet(makeUpper) 
greet(makeLower)
~~~

### Returning function

- We can also return a function as the result of another function as an object, and that makes the function a high order function.

~~~Python
def create_adder(x): 
    def adder(y): 
        return x + y 
    
    return adder 
    
add_15 = create_adder(15) 
    
print(add_15(10))
~~~

### Decorators

- Decorators are the most common use of higher-order functions in Python
- Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it.
- In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.

~~~Python
def hello_decorator(func): 
    
    def inner1(): 
        print("Hello, this is before function execution") 
    
        func() 
    
        print("This is after function execution") 
            
    return inner1 
    
def function_to_be_used(): 
    print("This is inside the function !!") 

function_to_be_used = hello_decorator(function_to_be_used) 
    
 
function_to_be_used() 
~~~

### Built-in Higher Order Functions
- Some of the built-in higher order functions are map(), filter, and reduce. 
- Lambda function can be passed as a parameter and the best use case of lambda functions is in functions like map, filter and reduce.

### Map Function
- The map() function is a built-in function that takes a function and iterable as parameters.

~~~Python
names = ['Wahko', 'Eisan', 'Mayphyo']  

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    

names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))
~~~
### Filter Function
- The filter() function calls the specified function which returns boolean for each item of the specified iterable (list). 
- It filters the items that satisfy the filtering criteria.

~~~Python
names = ['Wahko', 'Eisan', 'Mayphyo']  
def is_name_long(name):
    if len(name) > 5:
        return True
    return False

long_names = filter(is_name_long, names)
print(list(long_names))
~~~

### Reduce Function
- The reduce() function is defined in the functools module and we should import it from this module. 
- Like map and filter it takes two parameters, a function and an iterable. 
- However, it does not return another iterable, instead it returns a single value.

~~~Python 
import functools
numbers_str = ['1', '2', '3', '4', '5'] 
def add_two_nums(x, y):
    return int(x) + int(y)

total = functools.reduce(add_two_nums, numbers_str)
print(total)
~~~