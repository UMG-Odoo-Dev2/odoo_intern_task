# reduce() in Python
The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.This function is defined in “functools” module.

Working :  

    At first step, first two elements of sequence are picked and the result is obtained.
    Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
    This process continues till no more elements are left in the container.
    The final returned result is returned and printed on console.

### Example 1
```bash
    import functools
 

    lis = [1, 3, 5, 6, 2, ]
 
    print("The sum of the list elements is : ", end="")
    print(functools.reduce(lambda a, b: a+b, lis))
 
    print("The maximum element of the list is : ", end="")
    print(functools.reduce(lambda a, b: a if a > b else b, lis))

Output:The sum of the list elements is : 17
       The maximum element of the list is : 6
```
## Using Operator Functions

reduce() can also be combined with operator functions to achieve the similar functionality as with lambda functions and makes the code more readable.

### Example 3
```bash
    import functools
 
    import operator
 
    lis = [1, 3, 5, 6, 2, ]
 
    print("The sum of the list elements is : ", end="")
    print(functools.reduce(operator.add, lis))

    print("The product of list elements is : ", end="")
    print(functools.reduce(operator.mul, lis))

    print("The concatenated product is : ", end="")
    print(functools.reduce(operator.add, ["geeks", "for","geeks"])) 

Output:The sum of the list elements is : 17
The product of list elements is : 180
The concatenated product is : geeksforgeeks
```
## reduce() vs accumulate() 

Both reduce() and accumulate() can be used to calculate the summation of a sequence elements. But there are differences in the implementation aspects in both of these.  

- reduce() is defined in “functools” module, accumulate() in “itertools” module.
- reduce() stores the intermediate result and only returns the final summation value. Whereas, accumulate() returns a iterator containing the intermediate results. The last number of the iterator returned is summation value of the list.
- reduce(fun,seq) takes function as 1st and sequence as 2nd argument. In contrast accumulate(seq,fun) takes sequence as 1st argument and function as 2nd argument.

### Example 3
```bash
    import itertools
 

    import functools
 

    lis = [1, 3, 4, 10, 4]
 

    print("The summation of list using accumulate is :", end="")
    print(list(itertools.accumulate(lis, lambda x, y: x+y)))
 

    print("The summation of list using reduce is :", end="")
    print(functools.reduce(lambda x, y: x+y, lis))

Output:

The summation of list using accumulate is :[1, 4, 8, 18, 22]
The summation of list using reduce is :22
```
## reduce() function with three parameters

Reduce function i.e. reduce() function works with 3 parameters in python3 as well as for 2 parameters. To put it in a simple way reduce() places the 3rd parameter before the value of the second one, if it’s present. Thus, it means that if the 2nd argument is an empty sequence, then 3rd argument serves as the default one. 

 Here is an example :(This example has been take from the  functools.reduce() documentation includes a Python version of the function:
 ### Example 4
 ```bash
    def reduce(function, iterable, initializer=None):
        it = iter(iterable)
        if initializer is None:
            value = next(it)
        else:
            value = initializer
        for element in it:
            value = function(value, element)
        return value
 
    .
    tup = (2,1,0,2,2,0,0,2)
    print(reduce(lambda x, y: x+y, tup,6))

Output:15