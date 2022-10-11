# Higher Order Function in Python
> What is Higher Order Function in Python?
- A function can take one or more functions as parameters
- A function can be returned as a result of another function
- A function can be modified
- A function can be assigned to a variable

### Function as a Parameter

```py

# Function as a parameter

def sum_num(nums): # normal function
    return sum(nums)

def higher_order_func(func, lst): # function as a parameter
    summing = func(lst)
    return summing

result = higher_order_func(sum_num, [2,4,6,8])
print(result)

# Result => 20

```

### Function as a return value

```py

# Functoin as return value

def square(x): # a square function
    return x**2
def cube(x): # a cube function
    return x**3
def absolute(x): # a absolute function
    if x>=0:
        return x
    else:
        return -(x)

def high_ord_func(type): # returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = high_ord_func('square')
print(result(7))     # Result => 49
result = high_ord_func('cube')
print(result(7))     # Result => 343
result = high_ord_func('absolute')
print(result(-7))    # Result => 7
```

## Built-in Higher Order Function
- Python - Map Functon 
- Python - Filter Function
- Python - Reduce Function

### Python - Map Function

The map() function takes a function and iterable as parameters.

```py
# syntax
map(functon,iterable)
```
```py
nums = [1,3,5,7,9] # iterable

def square(n):
    return n**2
sq_nums = map(square,nums)
print(list(sq_nums), type(sq_nums))
# Result => [1, 9, 25, 49, 81] <class 'map'>


# With a lambda function
sq_nums = map(lambda n : n**2, nums)
print(list(sq_nums), type(sq_nums))
# Result => [1, 9, 25, 49, 81] <class 'map'>


fruits = ['Avocado','WaterMelon','Papaya','Guava']

def fruitUp(fruit):
    return fruit.upper()
result = list(map(fruitUp,fruits))
#result = list(map(lambda fruit : fruit.upper(), fruits))
print(result, type(result))
# Result => ['AVOCADO', 'WATERMELON', 'PAPAYA', 'GUAVA'] <class 'list'>
```
map() function iterate over a list and returns a new list

### Python - Filter Function

The filter() function calls the specified function which returns boolean for each item of the specified iterable (list)

```py
# syntax
map(functon,iterable)
```
```py
nums = [214, 333, 487, 967, 666, 555, 478]

def is_even(enum):
    if enum % 2 == 0:
        return True
    else:
        return False

even_num = list(filter(is_even, nums))
# with a lambda
#even_num = list(filter(lambda num : num%2 == 0, nums))
print(even_num, type(even_num))
# Result => [214, 666, 478] <class 'list'>
```

Filter filters out only the elements which the function returns true

### Python - Reduce Function

The reduce() apply a function to an iterable and reduce it to a single cumulative value. Performs function on first two elements and repeats process until 1 value remains. And we need to import `functools` module to use `reduce()` function

```py
# Example 1
import functools

letters = ['C','H','A','O','S']

# def redFun(x, y):
#     return x+y
# word = functools.reduce(redFun, letters)

word = functools.reduce(lambda x, y : x + y, letters)
print(word) 
# Result => CHAOS

```

```py
# Example 2
listNum = ['5','24','6','8','10']
redNum = functools.reduce(lambda x, y: x + y, listNum)
print(redNum)
# Result => 5246810

```
