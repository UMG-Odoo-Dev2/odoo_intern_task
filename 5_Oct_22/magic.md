# Magic or Dunder Methods in Python
- They start and end with the double underscores. 
- For example, when two numbers are added using the + operator, internally, the ```__add__()``` method will be called.
- Built-in classes in Python define many magic methods.
- Use the dir() function to see the number of magic methods inherited by a class. 
For example, the following lists all the attributes and methods defined in the ```int``` class.
```
>>> dir(int)
['__add__', '__and__', '__bool__',  '__class__', , '__dir__','__float__',  '__format__',   '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', etc....]
```
### ```__new__()``` method
- The ```__new__()``` magic method is implicitly called before the ```__init__()``` method. 
- It returns a new object, which is then initialized by ```__init__()```.
- For example;
~~~Python
class Employee:
    def __new__(cls):
        print ("__new__ magic method is called")
        inst = object.__new__(cls)
                return inst
    def __init__(self):
        print ("__init__ magic method is called")
        self.name='May Phyo'
    emp=Employee()
~~~
- The above example will produce the following output:
~~~Python
__new__ magic method is called
__init__ magic method is called
~~~
- Thus, the``` __new__()``` method is called before the ```__init__()``` method.


### ```__str__()``` method
- It is overridden to return a printable string representation of any user defined class.
- We have seen str() built-in function which returns a string from the object parameter. 
- For example, str(12) returns '12'. 
- When invoked, it calls the ```__str__()``` method in the int class.
~~~Python
class Employee:
    def __init__(self):
        self.name='Swati'
        self.salary=10000
    def __str__(self):
        return 'name='+self.name+' salary=$'+str(self.salary)
    e1=Employee()
    print(e1)
~~~
- The output result is :
```
 name=May Phyo salary=$10000
 ```
- Therefore, ```str()``` function internally calls the ```__str__()``` method defined in the Employee class. 
- This is why it is called a magic method.