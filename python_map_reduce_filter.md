# Python map() function
map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

Syntax :

    map(fun, iter)
Parameters :

    fun : It is a function to which map passes each element of given iterable.
    iter : It is a iterable which is to be mapped.

NOTE : You can pass one or more iterable to the map() function.

CODE 1
  
    def addition(n):
        return n + n
    
    numbers = (1, 2, 3, 4)
    result = map(addition, numbers)
    print(list(result))
Output :

    [2, 4, 6, 8]

# reduce() in Python

The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.This function is defined in “functools” module.

Working :  

- At first step, first two elements of sequence are picked and the result is obtained.
- Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
- This process continues till no more elements are left in the container.
- The final returned result is returned and printed on console.

Code 2

    import functools
 
    lis = [1, 3, 5, 6, 2, ]
 
    print("The sum of the list elements is : ", end="")
    print(functools.reduce(lambda a, b: a+b, lis))
 
    print("The maximum element of the list is : ", end="")
    print(functools.reduce(lambda a, b: a if a > b else b, lis))
Output

    The sum of the list elements is : 17
    The maximum element of the list is : 6
 
# filter() in python

The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.

syntax:

    filter(function, sequence)
    Parameters:
    function: function that tests if each element of a 
    sequence true or not.
    sequence: sequence which needs to be filtered, it can 
    be sets, lists, tuples, or containers of any iterators.
    Returns:
    returns an iterator that is already filtered.