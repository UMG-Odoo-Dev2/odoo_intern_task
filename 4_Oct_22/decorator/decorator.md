# Python Decorator
- Decorator ဆိုသည်မှာ userတစ်ယောက်ကို သူရဲ့structureကို without modifying ပြင်ဆင်ခြင်းမရှိဘဲနဲ့ ရှိပြီးသား object တစ်ခုတွင် new function အသစ်များကို add လုပ်နိုင်တဲ့ Pythonရဲ့ design patternတစ်ခုဖြစ်သည်။ 
- Decorators များကို များသောအားဖြင့် ***before the definition of a function you want to decorate*** ခေါ်ဝေါ်ကြပါသည်။
- ***Functions in Python*** are first class citizens. 
- ဆိုလိုတာက ၎င်းတို့သည် ***being passed as an argument*** argumentတစ်ခုအဖြစ် ဖြတ်သွားခြင်း၊ ***returned from a function*** functionတစ်ခုမှ returnပြန်ခြင်း၊ modifiedလုပ်ပြီး variableတစ်ခုကို assignedလုပ်ပေးခြင်း ကဲ့သို့သော လုပ်ဆောင်ချက်များကို supportပေးသည် ဟု ဆိုလိုသည်။

 ## Creating Decorators
 ```
 def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

def say_hi():
    return 'hello there'

decorate = uppercase_decorator(say_hi)
print(decorate())
```
- In this program, our decorator function takes a function as an argument.
- And then, define a function and pass it to our decorator.
- We learned earlier that we could assign a function to a variable. 
- We'll use that trick to call our decorator function.

- Output:
```
'HELLO THERE'
```

- However, Python provides a much easier way for us to apply decorators. 
- The @ symbol is used before the function that would be like to decorate. 

```
@uppercase_decorator
def say_hi():
    return 'hello there'

say_hi()
```
- Output:
```
'HELLO THERE'
```
## Applying Multiple Decorators to a Single Function
```
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
```
- Output:
```
400
```

- We can use multiple decorators to a single function. 
- However, the decorators will be applied in the order that we've called them.

## Accepting Arguments in Decorator Functions
```
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
```
- Output:
```
before Execution
Inside the function
after Execution
Sum = 3
```
- In this example, a keen difference in the parameters of the inner function may be noticed. 
- The inner function takes the argument as *args and **kwargs which means that a tuple of positional arguments or a dictionary of keyword arguments can be passed of any length. 
- This makes it a general decorator that can decorate a function having any number of arguments.

## Chaining Decorators
- In simpler terms chaining decorators means decorating a function with multiple decorators.
- Example:
```
# code for testing decorator chaining
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
```
Output:
```
400
```
- The above example is similar to calling the function as –
```
decor1(decor(num))
```
- In summary,decorators dynamically alter the functionality of a function, method, or class without having to directly use subclasses or change the source code of the function being decorated. 
- Using decorators in Python also ensures that our code is DRY(Don't Repeat Yourself). 
- Decorators have several use cases such as:
    - Authorization in Python frameworks such as Flask and Django
    - Logging
    - Measuring execution time
    - Synchronization