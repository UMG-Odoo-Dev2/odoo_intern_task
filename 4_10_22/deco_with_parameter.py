def decorator_func(x, y):
    print("In the decorator function")
 
    def Inner(func):
        print("In the inner function")

        def wrapper(*args, **kwargs):

            print("In the wrapper function")
            print("Summation of values - {}".format(x+y) )
            func(*args, **kwargs)

        return wrapper

    return Inner


@decorator_func(12,15)
def my_fun(*args):
    for txt in args:
        print(txt)

my_fun('Hello', 'Hey', 'Hi')