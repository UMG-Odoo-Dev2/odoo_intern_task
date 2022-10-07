# Magic methods in Python
- are the special methods that start and end with the double underscores like 

        __init__, __add__, __len__, __repr__ ,etc.
- are also called dunder methods

1. ***`__init__()`***
- is called every time an object is created from a class.
- lets the class initialize the object's attributes and serves no other purpose.
- is only used within classes.
~~~Python
        # declare our own string class
        class String:
      
            # magic method to initiate object
            def __init__(self, string):
                self.string = string
          
        # Driver Code
        if __name__ == '__main__':
      
            # object creation
            string1 = String('Hello')
  
            # print object location
            print(string1)

~~~

2. ***`__repr__()`***
- to represent a class's objects as a string
- can return any valid Python expression unlike `__str__()`

~~~Python
        def __repr__(self):
            return 'Object: {}'.format(self.string)
~~~

3. ***`__add__()`***
- gets called when we add two numbers using the + operator
- is used to add the attributes of the class instance

~~~Python
         num=10
         num + 5
~~~
- `num.__add__(5)` will give the same result like the above code

4. ***`__new__()`***
- will be called when instance is being created
- only the method which will be called first then `__init__ `will be called to initialize instance when you are creating instance
~~~Python
    class Employee:
    def __new__(cls):
        print ("__new__ magic method is called")
        inst = object.__new__(cls)
                return inst
    def __init__(self):
        print ("__init__ magic method is called")
        self.name='Satya'
~~~
- The above example will produce the following output when you create an instance of the **Employee** class.

~~~Python
    emp = Employee()
~~~
- Output:

        __new__ magic method is called<br>
        __init__ magic method is called

5. ***`__str__()`***
- to generate a printable string representation that is informal in nature and human-readable in nature
- always return a string

```
    num=12
    str(num)
```
- This code is equivalent to `int.__str__(num)`

6. ***`__dir__()`***
- implements the functionality of the dir() bit-in function
- dir() returns all(function, object, or variable) names in a given scope
- however, the magic method `__dir__()` converts any return value to a sorted  list 
~~~Python
    class Testing:
    def __dir__(self):
        return ['Orange','Apple','Banana']

    x = Testing()
    print(dir(x))
~~~
- The origin list ['Orange','Apple','Banana'] was automatically converted to the sorted list ['Apple', 'Banana', 'Orange']

7. ***`__del__()`***
- is a destructor method which is called as soon as all references of the object are deleted i.e when an object is garbage collected.

~~~Python
    class Example: 
    
    # Initializing
    def __init__(self): 
        print("Example Instance.")
  
    # Calling destructor
    def __del__(self): 
        print("Destructor called, Example deleted.") 
    
    obj = Example() 
    del obj 
~~~
8. ***`__len__()`***
-  to implement the len() function in Python because whenever we call the len() function then internally `__len__` magic method is called
~~~Python
    class MyClass:

	def __init__(self, item):
		self.item = item
	def __len__(self):
		return len(self.item)

    obj = MyClass("Hello World")
    print(obj.__len__()) #same as print(len(obj))
~~~
