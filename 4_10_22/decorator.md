# Decorator
- a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure

- Example 1:*Chaining Decorators*

        def decor1(func):
            def inner():
                x = func()
                return x * x
            return inner
 
        def decor(func):
            def inner():
                x = func()
                return 2 * x
            return inner
 
        @decor1
        @decor
        def num():
            return 10
 
        print(num())

Let's debug this example. In this example, we have two decorators called decor and decor1. And we also have a new function called num().

    @decor1
    @decor
    def num():
        return 10
 
    print(num())

is same as `decor1(decor(num))`. <br>So, when we call num(), the decor() function will run first cause of `@decor`. <br>`@decor` is just an easier way of saying `result = decor(num)`. It’s how we apply a decorator to a function. 

We have value '10' as an argument and after calling `@decor`, the result will be 20 (=2*10).

And then, we called the next decorator, `@decor1`. The result is 400(=20*20).

- Example 2: *Passing Parameters in Decorator*

        def decorator_func(x, y):
            print("In the decorator function") # 1st output
 
            def Inner(func):
                print("In the inner function") # 2nd output

                def wrapper(*args, **kwargs):

                    print("In the wrapper function") # 3rd output 
                    print("Summation of values - {}".format(x+y) ) # 4th ouput with the result 5
                    func(*args, **kwargs) # execute the function, final output

                return wrapper

            return Inner


        @decorator_func(12,15) # call decorator function with parameters
        def my_fun(*args):
            for txt in args:
                print(txt)

        my_fun('Hello', 'Hey', 'Hi')


