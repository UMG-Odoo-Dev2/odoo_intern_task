# Higher Order Function
- A function that takes other functions as arguments (or returns a function) is called a ***higher order function***.
- Properties of higher-order functions:
    - A function is an instance of the Object type.
    - The function in a variable can be stored.
    - The function as a parameter can be passed to another function.
    - The function from a function can be returned.
    - They can be stored in data structures such as hash tables, lists, etc ..
### Functions as arguments
~~~Python
def summation(nums): # normal function
    return sum(nums)

def main(f, *args): # function as an argument
    result = f(*args)
    print(result)

if __name__ == "__main__":
    main(summation, [2,3,4]) # output 9
~~~
- In this program, the functions can be passed as one of the arguments to another function.

### Having a function as a return value
```Python
def create_adder(x): 
    def adder(y): 
        return x + y 
    return adder 
    
add_9 = create_adder(9) 
    
print(add_9(10))  # output 19
```
- As functions are objects, a function from another function can be returned. 
- In this example, the ```create_adder``` function returns adder function.
- Thus, the higher order function is returning different functions depending on the passed parameter.

### Built-in Higher Order Functions
- Some of the built-in higher order functions are ``` map(), filter, and reduce```.
- Lambda function can be passed as a parameter and the best use case of lambda functions is in functions like map, filter and reduce.


> Python - Map Function
- The ```map()``` function is a built-in function that takes a function and iterable as parameters.
```Python
numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]

# Lets apply it with a lambda function
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
```
> Python - Filter Function
- The ```filter()``` function calls the specified function which returns boolean for each item of the specified iterable (list). 
- It filters the items that satisfy the filtering criteria.
```Python
# Filter long name
names = ['MayPhyoThu', 'ThinEiSan', 'WintWarKo', 'YeZawOo','AungMyatThu']  # iterable
def is_name_long(name):
    if len(name) > 9:
        return True
    return False

long_names = filter(is_name_long, names)
print(list(long_names))         # ['AungMyatThu']
```
> Python - Reduce Function
- The ```reduce()``` function is defined in the functools module and we should import it from this module.
- Like ```map``` and ```filter```, it takes two parameters, a function and an iterable. 
- However, it does not return another iterable, instead it returns a single value. 
- Example:
```Python
import functools
numbers_str = ['3', '4', '5', '6', '7']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)
total = reduce(add_two_nums, numbers_str)
print(total)    # Output 25 
```
