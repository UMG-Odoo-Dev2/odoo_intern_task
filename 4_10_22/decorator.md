# Decorator
- a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure

- Example:

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



