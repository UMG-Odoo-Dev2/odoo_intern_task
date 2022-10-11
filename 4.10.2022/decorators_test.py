
#_______________Using a variable as function object________
from re import X


def say(greeting):
    return greeting+", How are you?"

print("Regular Function Calling: "+say("Hello"))


speak=say

print(speak("Hi"))


#____________Passing function as an argument___________
def tell(greeting):
    return greeting.upper()

def shout(greeting):
    return greeting.lower()

def greet(func):
    greeting=func("How are you?")
    print(greeting)

greet(tell)
greet(shout)

#______________ Returning function from another function___________
def addition(num):
    def real_addition(adder):
        return num+adder
    return real_addition

add=addition(20)
print(add(30))

#____________________________

def hi_decorator(func):

    def wrapper():
        print("Beginning!")

        func()

        print("Ending!")
    return wrapper()
    # 1: return wrapper

# @hi_decorator (no need to call hi_decorator , call do_function)
def do_function():
    print("inside the function!")

hi_decorator(do_function)
#1: call_wrapper=hi_decorator(do_function)
#   call_wrapper()

#____________Chaining Decorator_______

def first_decor(func):

    def wrapper():
        x=func()
        return x**x

    return wrapper

def second_decor(func):

    def wrapper():
        x=func()
        return x*10

    return wrapper

@second_decor
@first_decor
def para_function():
    return 3

#second_decor(first_decor(para_function))

print(para_function())

#____________________

def case_decorator(func):

    def case_wrapper():
        return func().upper()

    return case_wrapper

def case_change():
    return "Thanks God It's Friday"

sentence=case_decorator(case_change)

print(sentence())
print(type(sentence))
#_______________________________

def case_decorator(func):

    def case_wrapper():
        return func().upper()

    return case_wrapper

@case_decorator
def case_change():
    return "Thanks God It's Friday"

print(case_change())

#_______________________

#decorator
def my_decorator(*persons,**fruits):

    print("Inside decorator")
    #inner
    def my_wrapper(func):
        begin()
        func()
        like()
        end()

    def like():
        print(persons[0]," likes ",fruits['like']) # kwargs['key'], args[0]
        
    def begin():
        print("My wrapper begins")

    def end():
        print("My Wrapper ends")

    return my_wrapper


person_name=input("Enter a name:")
fruit_name=input("Enter a fruit name:")

@my_decorator(person_name,like=fruit_name)
def my_fun():
    print("Inside my function")



