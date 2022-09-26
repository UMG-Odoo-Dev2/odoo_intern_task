# Python map() function
map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
### Syntax:
```bash
map(fun, iter)
```
Parameters:
```bash
fun : It is a function to which map passes each element of given iterable.
iter : It is a iterable which is to be mapped.
```
### Returns:
```bash
Returns a list of the results after applying the given function  
to each item of a given iterable (list, tuple etc.) 
```
### NOTE : The returned value from map() (map object) then can be passed to functions like list() (to create a list), set() (to create a set) .
Example1:
```bash
    def addition(n):
        return n + n
  
    numbers = (1, 2, 3, 4)
    result = map(addition, numbers)
    print(list(result))

Output:[2, 4, 6, 8]
```
#### Example 2
- We can also use lambda expressions with map to achieve above result.
```bash
    numbers = (1, 2, 3, 4)
    result = map(lambda x: x + x, numbers)
    print(list(result))

Output:[2, 4, 6, 8]
```
#### Example 3
```bash
    numbers1 = [1, 2, 3]
    numbers2 = [4, 5, 6]
  
    result = map(lambda x, y: x + y, numbers1, numbers2)
    print(list(result))

Output:[5, 7, 9]
```

#### Example 4
```bash
    l = ['sat', 'bat', 'cat', 'mat']
    test = list(map(list, l))
    print(test)

Output:[['s', 'a', 't'], ['b', 'a', 't'], ['c', 'a', 't'], ['m', 'a', 't']]