def uppercase_decorator(function):# First Decorator
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

def split_string_decorator(function):# Second decorator
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string_decorator
@uppercase_decorator 
def greeting():
    return 'This is multi decorator'
print(greeting())
