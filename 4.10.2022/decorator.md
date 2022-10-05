# **Decorator**
- A decorator is a design pattern.
- a function that takes another function as its argument, and returns yet another function. 
- allows a user to add new functionality to an existing object without modifying its structure.
- using the decorators ensures that your code is DRY (Don't repeat yourself).
- Example : 
~~~Python
        def hello_decorator(func):
            def inner1(*args,**kwargs):
                print("before Execution")

                # get the return value 
                returned_value = func(*args,**kwargs)
                print("after Execution")

                # return the value to the original frame
                return returned_value
         
            return inner1
 
 
        # add decorator to the function**

        @hello_decorator
        def sum_two_numbers(a, b):
        print("Inside the function")
        return a + b
 
        a, b = 1,2
 
        # get the value through return of the function**

        print("Sum =", sum_two_numbers(a, b))
~~~

## **Chaining Decorator**
- means decorating a function with multiple decorators.
- Example : 
~~~Python

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
        
        print(num()) // output is 400
~~~
- The above example is similar to calling the function as –


        decor1(decor(num))

## **Passing parameter in Decorator**

~~~Python
    def decorator(*args, **kwargs):
        print("Inside decorator")
        
        def inner(func):
            
            # code functionality here
            print("Inside inner function")
            print("I like", kwargs['like'])
            
            func()
            
        # returning inner function   
        return inner
    
    @decorator(like = "sandwish")
    def my_func():
        print("Inside actual function")
~~~
Output : 
 
    Inside decorator
    Inside inner function
    I like sandwish
    Inside actual function

In above example: 
- first run decorator function
- second run inner function,in this function print the vlaue of paramenter of decorator and call the actual function.
- finally print the result of actual function.