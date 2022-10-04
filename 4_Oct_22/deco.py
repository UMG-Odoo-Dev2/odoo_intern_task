#TESTING 1
# def decor1(func):
#     def inner():
#         x = func()
#         return x * x
#     return inner
 
# def decor(func):
#     def inner():
#         x = func()
#         return 2 * x
#     return inner
 
# @decor1
# @decor
# def num():
#     return 10
 
# print(num())


##Testing 2
def hello_decorator(func):
    def inner1(*args, **kwargs):
         
        print("before Execution")
         
        # getting the returned value
        returned_value = func(*args, **kwargs)
        print("after Execution")
         
        # returning the value to the original frame
        return returned_value
         
    return inner1
 
 
# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b
 
a, b = 1, 2
 
# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))


