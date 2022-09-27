# **LAMBDA**

### **Lambda function**
-  Single-Line function
-  can take any number of arguments, but can only have one expression.<br>
- reduces the number of lines of code.
    
     **Syntax**

        lambda argument(s): expressoin

        lambda x: x

- In the example above, the expression is composed of:

    1. The keyword: lambda<br>
    2. A bound variable: x<br>
    3. A body: x
- takes in other functions as arguments<br>
Example : higher-order-function

        high_ord_func = lambda x, func: x + func(x)
        high_ord_func(2, lambda x: x * x) # return 6
        high_ord_func(2, lambda x: x + 3) # return 7

#### **Immediately Invoked Function Expression (IIFE)**
Example:

        (lambda x, y: x + y)(2, 3) # return 5

### **Map**
- The built-in function map() takes a function as a first argument and applies it to each of the elements of its second argument, an iterable.<br>
_Examples of iterable are : lists, tuples, sets, dictionaries, strings ect._

        x=list(map(lambda x: x.capitalize(), ['cat', 'dog', 'cow']))
        print(x) 

        # return ['Cat', 'Dog', 'Cow']

- In above example need to invoke list() to convert the iterator returned by map() into an expanded list. 
- If we don't invoke list (or) other iterables , the result is as follow.

        y=map(lambda x: x.capitalize(), ('cat', 'dog', 'cow'))
        print(y) 
        # return <map object at 0x0000021B42C21400>

### **Filter**
- can be converted into a list comprehension.
-  takes a predicate as a first argument and an iterable as a second argument.

        even = lambda x: x%2 == 0
        list(filter(even, range(11)))
        # [0,2,4,6,8,10]

- filter() aslo returns an iterator, hence the need to invoke the built-in type list.

### **Redeuce**
- Its first two arguments are respectively a function and an iterable as map() and filter().
- It may also take an initializer as a third argument that is used as the initial value of the resulting accumulator.

        import functools
        pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
        functools.reduce(lambda acc, pair: acc + pair[0], pairs, 1)

        # 7
