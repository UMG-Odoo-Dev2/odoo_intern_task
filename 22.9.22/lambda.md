# Python Lambda Functions
- They are anonymous function
- As we already know that the def keyword is used to define a normal function in Python. 
- Similarly, the lambda keyword is used to define an anonymous function in Python.

## Python Lambda Function Syntax
Syntax: 
```
lambda arguments: expression
```
- Example: 
   ``` 
   str1 = 'GeeksforGeeks' 
   new_str = lambda string:string.upper[::-1]
   print(new_str(str1))
   ```
- Output
   ```
   SKEEGROFSKEEG
   ```
- By using lambda function, it supports single line statements that returns some value.
- Good for performing short operations/data manipulations.
- It can sometime reduce the readability of code.
- It can be used along with built-in functions like <span style="color:green;font-weight:700;font-size:15px">filter(), map(), reduce().</span>

## Using lambda() Function with filter()
- filter() function takes in a function and a list as arguments.
- The function is called with all the items in the list and a new list is returned which contains items for which the function evaluates to True.

- Example:
```
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list)
```
- Output:
```
[4, 6, 8, 12]
```
## Using lambda() Function with map()
- The map() function also takes in a function and a list.
- The function is called with all the items in the list and a new list is returned which contains items returned by that function for each item.
- Example:
```
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))
print(new_list)
```
- Output:
```
[2, 10, 8, 12, 16, 22, 6, 24]
```