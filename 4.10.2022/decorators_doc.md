## Decorators
- A function that can take a function as an argument and extend its functionality and return a modified function with extended functionality.
- Before creating Python decorators, We need to understand "*How functions work in Python*".
- Decorators are usually called before the definition of a function we want to decorate.
- To create a decorator function, we need an outer function with an inner wrapper function.
```py
def case_decorator(func):

    def case_wrapper():
        return func().upper()

    return case_wrapper

def case_change():
    return "Thanks God It's Friday"

sentence=case_decorator(case_change)

print(sentence())
print(type(sentence))
```
- Code Explanation: 
  - a function `case_change()` is passed as a parameter to a decorator function `case_decorator()`.
  - a variable `sentence` receives a return function object type and a wrapper function `case_function()` is called.
  - `case_function()` converts a sentence into upper format. 
  ```
  output:
    THANKS GOD IT'S FRIDAY
    <class 'function'>
  ```
- Python provides a much easier way, Using @ symbol before the function we would like to decorate, to apply decorators.
```py
def case_decorator(func):

    def case_wrapper():
        return func().upper()

    return case_wrapper

@case_decorator
def case_change():
    return "Thanks God It's Friday"

print(case_change())
```
```
output:
    THANKS GOD IT'S FRIDAY
```
- ***Chaining decorator*** : applying more than one decorators inside a function.
```py
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

```
- Code Explanation:
    - for a function `para_function()`, we are applying 2 decorators.
    - First, inner decorator `first_decor()` is called with a function `para_function()` as a parameter.
    - Then, outer decorator `second_decor()` is called with a return value of inner decorator as a parameter.
     
    ```
    output:
        270
- ***Decorators with parameters*** is similar to normal decorators.
```py
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
```
- Code Explanation:
    - the two variable `person_name` and `fruit_name` receives two inputs from keyboard.
    - `person_name` and `fruit_name` is passed as two parameters to a decorator function `my_decorator()` and a inner function `my_wrapper()` is called with a function `my_fun()` as a parameter.
    - In `my_wrapper()` function, three inner functions *begin(), like(), end()* and a parameter function *my_fun()* is called.
    ```
    output:
    Enter a name:YZO
    Enter a fruit name:Watermelon
    Inside decorator
    My wrapper begins
    Inside my function
    YZO  likes  Watermelon
    My Wrapper ends
    ```



