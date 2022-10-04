# def parent():
#     print("Printing from the parent() function")

#     def first_child():
#         print("Printing from the first_child() function")

#     def second_child():
#         print("Printing from the second_child() function")

#     second_child()
#     first_child()
# parent()
# #first_child()

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# def say_whee():
#     print("Whee!")

# say_whee = my_decorator(say_whee)
# say_whee()



# from datetime import datetime

# def not_during_the_night(func):
#     def wrapper():
#         if 7 <= datetime.now().hour < 15:
#             func()
#         else:
#             pass  # Hush, the neighbors are asleep
#     return wrapper

# def say_whee():
#     print("Whee!")

# say_whee = not_during_the_night(say_whee)
# say_whee()



# def do_twice(func):
#     def wrapper_do_twice():
#         func()
#         func()
#     return wrapper_do_twice


# Testing_1
#Treating the functions as objects
# def shout(text):
#     return text.upper()
# print(shout('Hello'))
# yell = shout
# print(yell('Hello'))


# Testing_2 
# Passing the function as an argument 
# def shout(text):
#     return text.upper()
# def whisper(text):
#     return text.lower()
# def greet(func):
#     # storing the function in a variable
#     greeting = func("""Hi, I am created by a function passed as an argument.""")
#     print (greeting)
 
# greet(shout)
# greet(whisper)


#Functions Returning other Functions
# def hello_function():
#     def say_hi():
#         return "Hi"
#     return say_hi
# hello = hello_function()
# print(hello())


#Nested Functions have access to the Enclosing Function's Variable Scope
# def print_message(message):
#     "Enclosong Function"
#     def message_sender():
#         "Nested Function"
#         print(message)

#     message_sender()

# print_message("Some random message")