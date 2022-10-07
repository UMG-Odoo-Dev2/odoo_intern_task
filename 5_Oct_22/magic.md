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
### 1. ```__new__()``` method
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


### 2. ```__str__()``` method 
- The ```__str__``` gives a human-readable output of the object.
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
- In this program ``` __str__()``` method in the Employee class to return a string representation of its object.

### 3. ```__add__()``` method
- This method specifies what happens when you call + on two objects.
- ```__add__()``` method adds two objects and returns a new object as a resultant object in Python.
- The below example returns a new object,

~~~Python
class MPT:
  
    def __init__(self, val):
        self.val = val
          
    def __add__(self, val2):
        return MPT(self.val + val2.val)
  
obj1 = MPT("May")
obj2 = MPT("PhyoThu")
obj3 = obj1 + obj2
print(obj3.val)


##In another way that is not using __add__ method
class MPT1:
    def __init__(self, val):
        self.val = val
  
obj1 = MPT1("May")
obj2 = MPT1("PhyoThu")
obj3 = obj1 + obj2
print(obj3.val)
~~~
- First output for this program is:
```
MayPhyoThu
```
- By not using ```__add__``` method, the output will be: 

```
    obj3 = obj1 + obj2
TypeError: unsupported operand type(s) for +: 'MPT1' and 'MPT1'
```
### 4. ```__init__ method```
- The ```__init__``` method is used to initialize objects. 
- This method is used to implement the constructor of the object.
- For Example:
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
- - This output will be,
```
<__main__.String object at 0x0000025EFDEE6160>
```
- The above program prints only the memory address of the string object.
- Let’s add a ```__repr__``` method to represent our object.

### 5. ```__repr__``` method
~~~Python
class String:
      
    # magic method to initiate object
    def __init__(self, string):
        self.string = string
          
    # print our string object
    def __repr__(self):
        return 'Object: {}'.format(self.string)
  
# Driver Code
if __name__ == '__main__':
      
    # object creation
    string1 = String('Hello')
  
    # print object location
    print(string1)
~~~
- The output will be:
```
Object: Hello
```
