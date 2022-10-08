# Decorator in Python
> We must understand first that everything in Python is Object.
```
# Treating the function as object
def shout(text):
    return(text.upper())

print(shout("i hate u!!"))
yell=shout

print(yell("i hate u too!!"))
```
- Output
```
I HATE U!!
I HATE U TOO!!
```
> In Python, we can also define a Function inside a Function.
```
def first_fun(msg):
    greet = "Hello"
    def second_fun():
        print(greet,msg)
    second_fun()
first_fun("Python is Suck!!!!")
```
- Output
```
Hello Python is Suck!!!!
```

> Functions can also return another function as a value.

```
def first_fun(msg):
    greet = "Hello"
    def second_fun():
        print(greet,msg)
    return second_fun
func = first_fun("Python is Difficult!!!!")
func()
```
- Output
```
Hello Python is Difficult!!!!
```
> What is Decorator?
- A Python Decorator is a function that takes in a function, add some functionality to it and returns the origin function.

```
def display_fun(func):
    def inner():
        print("Executing", func.__name__, "function")
        func()
        print("Finished Execution!!!!")
    return inner

@display_fun
def printer():
    print("CHAOS Running!!!")
printer()
```
- Output
```
Executing printer function
CHAOS Running!!!
Finished Execution!!!!
```
- `@display_fun` is equavalant to `printer = display_fun(printer)`
- first `display_fun` is called with parameter `printer` function 
- and then `inner` function return to its called function and called function is `printer`
- and then execute inner function print the first line and then see the function called `func()` so the printer function execute and print `CHAOS Running!!!`
- and then print the last line and execution finished

> Decorator with Parameter

```
def decorate_func(x, y):
	print("Decorate Function")
    print(x,y)
	def Inner(pick):
		print("Inner")

		def wrapper(*args, **kwargs):
			print(type(pick))
			print("Inside Execution Function")
			print("Sum of value - {}".format(x+y))

			pick(*args, **kwargs)
			print(type(pick))
		return wrapper

	return Inner

@decorate_func(13,25)
def fun_arg(*args):
	for you in args:
		print(you)

fun_arg('You','Broke','Me','First')
```
- *Code Explanation*
  - firstly called decorator function `@decorate_func(13,25)` with argument `(13,25)` and accept arguments with `(x,y)` parameter, its inner function is call with arguments `fun_arg('You','Broke','Me','First')`
  - inner function return and print
   Inner and wrapper function return and execute its inside function
  - wrapper function accept *args and **kwargs from its return function inner, inner is called with `pick(*args, **kwargs)` and `fun_arg` function's arguments is passed 
- *Output*
```
Decorate Function
13 25
Inner
<class 'function'>
Inside Execution Function
Sum of value - 38
You
Broke
Me
First
<class 'function'>
```
- Another way of using decorator
```
def fun_arg(*args):
	for you in args:
		print(you)

decorate_func(13,25)(fun_arg)('You','Broke','Me','First')
```

> Chaining Decorator

```
def first_decor(func):
    def inner():
        x = func()
        return x * x
    return inner

def second_decor(funs):
    def inner():
        x = funs()
        return x * 20
    return inner

@first_decor # second execute
@second_decor # first execute
def para_pass_fun():
    return 20
print(para_pass_fun())
```
- *Code Explanation*
  - There is two decorator function and inner decorator `@second_decor` function is called first and its function execute and executed result carry to outer decorator `@first_decor` and its function is executed with carried result 

- *Output*
```
print(para_pass_fun()) => 160000
```

