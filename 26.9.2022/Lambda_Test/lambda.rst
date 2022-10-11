#############
Lambda
#############

* An small anonymous function (a function without a name)
* No more than one line
* Like a normal function, multile arguments with one expression
* No return keyword defined explicitly because it does return an object by default
* In Python, lambda functions are used when a nameless function is required for a short period of time
* Syntax: lambda *arguments* : *expression*
  
  >>> square=lambda x:x*2
  >>> print("Square is ",square(2))

* Lambdas support IIFE (Immediately Invoked Function Expression) that means that a lambda function is callable as soon as it is defined
* Syntax: (lambda *parameter* : *expression*) (*argument*)

  >>> (lambda x:x*2)(2)

* Lambda functions are used as an argument to a higher-order function ( a function that takes in other functions as arguments)
* Lambda functions are used along with built-in functions like filter(), map(), reduce()
* filter() : to select some particular elements from a sequence of elements
* Syntax: filter (*function, iterable*)

  >>> my_list=[1,2,3,4,5,6,7,8,9,10]
  >>> new_list=list(filter(lambda x:(x%2==0),my_list))
  >>> print(new_list)

* map(): to apply a particular operation to every element in a sequence
* Syntax: map (*function, iterable*)

  >>> my_list=[1,2,3,4,5,6,7,8,9,10]
  >>> new_list=list(map(lambda x:x*x,my_list))
  >>> print(new_list)

* reduce(): to apply a particular operation to every element in a sequence. However, it differs from the map in its working
* Syntax: reduce(*function, iterable*)

  >>> from functools import reduce
  >>> my_list=[1,2,3,4,5,6,7,8,9,10]
<<<<<<< HEAD
  >>> reduced=list(reduce(lambda x,y:x*y,my_list))
  >>> print(reduced)
=======
  >>> new_list=list(reduce(lambda x,y:x*y,my_list))
  >>> print(new_list)
>>>>>>> 0c915ca04e9305325e7bfae7d98aa8e46be9f264

* Do not write complicated lambda functions in a production environment because it will be difficult for code-maintainers.
