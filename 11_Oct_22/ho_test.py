# Functions as arguments Example (1)
from functools import reduce


def summation(nums): # normal function
    return sum(nums)

def main(f, *args): # function as an argument
    result = f(*args)
    print(result)

if __name__ == "__main__":
    main(summation, [2,3,4]) # output 9


#Having a function as a return value Example (2)
def create_adder(x): 
    def adder(y): 
        return x + y 
    return adder    
add_9 = create_adder(9)    
print(add_9(10))  # output 19



# Python - Map Function Example (3)
numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# Lets apply it with a lambda function
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]


# Python - Filter Function Example (4)
names = ['MayPhyoThu', 'ThinEiSan', 'WintWarKo', 'YeZawOo','AungMyatThu']  # iterable
def is_name_long(name):
    if len(name) > 9:
        return True
    return False

long_names = filter(is_name_long, names)
print(list(long_names))         # ['AungMyatThu']


# Python - Reduce Function Example (5)
import functools
numbers_str = ['3', '4', '5', '6', '7']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)
total = reduce(add_two_nums, numbers_str)
print(total)    # Output 25 


# Applying Multiple Decorators to a Single Function
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

@split_string_decorator
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON