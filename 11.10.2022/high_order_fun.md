# **Higher Order Function**
- contains other functions as a parameter.
- returns a function as an output.

#### **Properties of higher-order functions:**
- A function is an instance of the Object type.
- You can store the function in a variable.
- You can pass the function as a parameter to another function.
- You can return the function from a function.
- You can store them in data structures such as hash tables, lists, ...

#### **Functions as objects**
- a function can be assigned to a variable.

    Example :
    ~~~Python
    def shout(text): 
    return text.upper() 
    
    print(shout('Hello')) 
    
    # Assigning function to a variable
    yell = shout 
    
    print(yell('Hello')) 
    ~~~

    Outputs : 

        HELLO
        HELLO

#### **Passing Function as an argument to other function**
- Functions are like objects in Python, therefore, they can be passed as argument to other functions.

    Example :
    ~~~Python
    # can be passed as arguments to other functions 
    def shout(text): 
        return text.upper() 
        
    def whisper(text): 
        return text.lower() 
        
    def greet(func): 
        # storing the function in a variable 
        greeting = func("Hi, I am created by a function \
    passed as an argument.") 
        print(greeting)  
        
    greet(shout) 
    greet(whisper)
    ~~~
    Outputs : 

        HI, I AM CREATED BY A FUNCTION PASSED AS AN ARGUMENT.
        hi, i am created by a function passed as an argument.

#### **Function as a return value**

Example :
```py
    def square(x):          # a square function
        return x ** 2

    def cube(x):            # a cube function
        return x ** 3

    def absolute(x):        # an absolute value function
        if x >= 0:
            return x
        else:
            return -(x)

    def higher_order_function(type): # a higher order function returning a function
        if type == 'square':
            return square
        elif type == 'cube':
            return cube
        elif type == 'absolute':
            return absolute

    result = higher_order_function('square')
    print(result(3))       # 9
    result = higher_order_function('cube')
    print(result(3))       # 27
    result = higher_order_function('absolute')
    print(result(-3))      # 3
    print(result(3))       # 3
```
In above example, the higher order function is returning different functions depending on the passed parameter.

## **Built-in Higher Order Functions**
- A few useful higher-order functions are map(), filter(), and reduce().
- Lambda function can be passed as a parameter and the best use case of lambda functions is in functions like map, filter and reduce.

#### **1) Python - Map Function**

The map() function is a built-in function that takes a function and iterable as parameters.

    # syntax
    map(function, iterable)
Example :
~~~Py
    numbers = [1, 2, 3, 4, 5] # iterable

    def square(x):  # function
        return x ** 2

    numbers_squared = map(square, numbers)
    print(list(numbers_squared))    # [1, 4, 9, 16, 25]

    # apply it with a lambda function
    numbers_squared = map(lambda x : x ** 2, numbers)
    print(list(numbers_squared))    # [1, 4, 9, 16, 25]
~~~

#### **2) Python - Filter Function**
The filter() function calls the specified function which returns boolean for each item of the specified iterable (list). It filters the items that satisfy the filtering criteria.

    # syntax
    filter(function, iterable)

Example :
~~~Py
    # Filter long name
    names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable
    def is_name_long(name): # function
        if len(name) > 7:
            return True
        return False

    long_names = filter(is_name_long, names)
    print(list(long_names))         # ['Asabeneh']
~~~

#### **3) Python - Reduce Function**

The reduce() function is defined in the functools module and we should import it from this module. It does not return another iterable, instead it returns a single value.

    # syntax
    filter(function, iterable)

Example :
~~~Py
    numbers_str = ['1', '2', '3', '4', '5','6']  # iterable
    def add_two_nums(x, y):      # function
        return int(x) + int(y)

    total = reduce(add_two_nums, numbers_str)
    print(total) # 21
~~~