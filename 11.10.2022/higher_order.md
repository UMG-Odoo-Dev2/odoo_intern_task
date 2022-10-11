## Higher Order Functions
In Python, higher order function is a function that takes one or more functions as parameters and/or return a function as a result.

```py
def odd_or_even(num):
    if (num % 2) == 0:
        return "even"
    else:
        return "odd"

def higher_order_function(func,number): #takes a function as a parameter
    confirm=func(number)
    return confirm  #returns a function

num=int(input("Is this number odd or even?\n"))
result=higher_order_function(odd_or_even,num)
print(num," is a ",result," number")
```
Code Explanation:
- takes a number from keyboard
- calls a higher order function `higher_order_function`() with two arguments: a function `odd_or_even`() and a user input `num`.
- In higher order function, a parameter function `odd_or_even`() is called with a parameter int variable `num`.
- `odd_or_even`() will decide a number is odd or even.
- a return value of `odd_or_even`() is assigned to a variable `confirm` and then a return value of `higher_order_function`() is assigned to a variable `result`.

Some of the built-in higher order functions are `map`(), `filter`() and `reduce`().
- `map`(): takes a functon and iterable as parameter
```
map:
[
    a -> n
    b -> o
    c -> p
]
```

```py
#syntax map(function,iterable)

or_list=[1,2,3,4,5] #iterable
def cube(n):             
    return n**3

#with a normal Function
cube_list=map(cube,or_list) 
print(list(cube_list))

#with a lambda function
lcube_list=map(lambda n:n**3,or_list)
print(list(lcube_list))
```
- `filter`(): takes a function with a condition which returns a boolean for each item of the specified iterable.

```
filter:
[
    a -> a
    b
    c -> c
]
```
```py
#syntax filter(function,iterable)

num_list=[1,2,3,4,5] #iterable
def is_odd(n):
    if(n%2!=0):     #condition
        return True     #return boolean
    else:
        return False

#with a normal function
odd_list=filter(is_odd,num_list)
print(list(odd_list))

#with a lambda function
lodd_list=filter(lambda n:(n%2)!=0,num_list)
print(list(lodd_list))
```
- `reduce`(): is defined in the functools module and imported from this module.
    - Like map and filter it takes two parameters, a function and an iterable.
    - However, it does not return another iterable, instead it returns a single value.
```
reduce:
[
    a       
    b
    c
]

for sum -> ((a+b)+c)
```
```py
org_list=[1,2,3,4,5] #iterable

# a function with two parameters
def is_sum(x,y):
    return x+y

#two importing ways

#with a normal function
from functools import reduce
sum=reduce(is_sum,org_list)
print(sum)

#with a lambda function
import functools
lsum=functools.reduce(lambda x,y:x+y,org_list)
print(lsum)
```
