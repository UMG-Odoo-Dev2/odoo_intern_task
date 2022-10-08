from re import X
#Teating the function as objects
def shout(text):
    return(text.upper())

print(shout("i hate u!!"))
yell=shout

print(yell("i hate u too!!"))

# Define a Function inside a Function
def first_fun(msg):
    greet = "Hello"
    def second_fun():
        print(greet,msg)
    second_fun()
first_fun("Python is Suck!!!!")

# Function can also return another function as a value
def first_fun(msg):
    greet = "Hello"
    def second_fun():
        print(greet,msg)
    return second_fun
func = first_fun("Python is Difficult!!!!")
func()

def display_fun(func):
    def inner():
        print("Executing", func.__name__, "function")
        func()
        print("Finished Execution!!!!")
    return inner

@display_fun
def printer():
    print("CHAOS Running!!!")
printer()


# Inner Function
def parent():
    print("This is parent function!")

    def first_child():
        print("This is first child!")

    def second_child():
        print("This is second child")

    second_child()
    first_child()
parent() # won't exucute inner func, if don't call parent function

# Returning Functions from Functions
def parent(num):
    def first_child():
        return "Hi! I'm Leo"
    def second_child():
        return "Call me Jack"
    
    if num == 1:
        return first_child
    else:
        return second_child

first = parent(3)
second = parent(1)
print(type(first), first())
print(type(second), second())

# Simple Decorator
def my_decorator(func):
    def wrapper():
        print("Something happen before fun called.")
        func()
        print("Something happen after fun called.")
    return wrapper()

@my_decorator
def say_haha():
    print("No HaHa")

#say_haha = my_decorator(say_haha)

# Chaining Decorator
def first_decor(func):
    def inner():
        x = func()
        return x * x
    return inner

def second_decor(funs):
    def inner():
        x = funs()
        return x * 20
    return inner

@first_decor # second execute
@second_decor # first execute
def para_pass_fun():
    return 20
#para_pass_fun = first_decor(second_decor(para_pass_fun))
print(para_pass_fun())
print(int(X))


# def hello_decorator(func):
#     def inner1():
#         print("Hi, This is function before execution")
#         func()
#         print("This is after function execution")
#     return inner1

# def function_to_be_used():
#     print("This is inside the functon !!")

# function_to_be_used=hello_decorator(function_to_be_used)
# function_to_be_used()