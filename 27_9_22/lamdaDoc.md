# ***Lambda***
### A lambda function  
- is a small anonymous function
- can take any number of arguments, but can only have one expression
- are defined using the ***lambda*** keyword.

    __`lambda arguments : expression `__
- can be used when an anonymous function is required for a short period of time
- is frequently used with higher-order functions, which take one or more functions as arguments or return one or more functions
- can be a higher-order function by taking a function (normal or lambda) as an argument like

### A lambda function has the following characteristics:

- It can only contain expressions and can’t include statements in its body.
- It is written as a single line of execution.
- It does not support type annotations.
- It can be immediately invoked (IIFE)


## Alternatives to Lambdas
Higher-order functions like map(), filter(), and functools.reduce() can be converted to more elegant forms with slight twists of creativity, in particular with list comprehensions or generator expressions.

### Map
- The built-in function map() takes a function as a first argument and applies it to each of the elements of its second argument, an iterable. Examples of iterables are strings, lists, and tuples.
- map() returns an iterator corresponding to the transformed collection
- Example:<br>

            list(map(lambda x: x.capitalize(), ['cat', 'dog', 'cow']))

- We need to invoke list() to convert the iterator returned by map() into an expanded list that can be displayed in the Python shell interpreter
- The output of the example is a list that transformed a new list with each string capitalized like this: ['Cat', 'Dog', 'Cow']

### Filter
- The built-in function filter() can be converted into a list comprehension
- It takes a predicate as a first argument and an iterable as a second argument
- It builds an iterator containing all the elements of the initial collection that satisfies the predicate function
- Example:

            even = lambda x: x%2 == 0
            list(filter(even, range(11)))

- The output is a list hat filters all the even numbers in a given list of integers

### Reduce
- 
- The built-in function reduce()'s first two arguments are respectively a function and an iterable
-  It may also take an initializer as a third argument that is used as the initial value of the resulting accumulator
- Example:

            import functools
            pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
            functools.reduce(lambda acc, pair: acc + pair[0], pairs, 0)
- In this example we have three arguments ,function ,iterable list and initializer for acc 0. Then, we will add the values of pair[0] to acc and the result will be 6.