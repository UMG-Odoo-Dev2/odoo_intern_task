# **Magic Method in Python**
- Magic methods are special methods in python that have ***double underscores*** (dunder) on both sides of the method name. 
- Magic methods are predominantly used for operator overloading
( ***The + operator is also defined as a concatenation operator in string, list and tuple classes. We can say that the + operator is overloaded*** ).

    Example : 

        __init__,__add__,__str__,__bool__,etc.


1. The `__init__` method for initialization is invoked without any call, when an instance of a class is created.
2. The `__repr__` is a special method used to represent a class’s objects as a string. `__repr__` is called by the repr() built-in function. You can define your own string representation of your class objects using the `__repr__` method.

    Example :
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

3. The `__add__` method is a magic method which gets called when we add two numbers using the + operator.

    Example : add String to Object
    ~~~Python
        class MyClass:

    def __init__(self, str):
        self.string = str 
          
    def __repr__(self):
        return 'Object: {}'.format(self.string)
          
    def __add__(self, other):
        return self.string + other

    if __name__ == '__main__':
        obj = MyClass('Hello')
        print(obj +' World')
    ~~~
    In above example : if we don't use the `__add__` method, 
        
        TypeError: unsupported operand type(s) for +: 'MyClass' and 'str'

4. The `__delete__` is used to delete the attribute of an instance i.e removing the value of attribute present in the owner class for an instance.
5. The `__del__` is a destructor method which is called as soon as all references of the object are deleted i.e when an object is garbage collected.

    Example : 
    ~~~Python
        class Example: 

            def __init__(self): 
                print("Example Instance.")
        
            def __del__(self): 
                print("Destructor called, Example deleted.") 
            
        obj = Example() 
        del obj
        print(obj)
    ~~~
    In above example: 
    - the output before del obj is 

        - Example Instance.
        - <__main__.Example object at 0x0000013E0A395A60>
        - Destructor called, Example deleted.

    - the output after del obj is 

        - Example Instance.
        - Destructor called, Example deleted.
        - NameError: name 'obj' is not defined.<br><br>

6. The `__str__` method is overridden to return a printable string representation of any user defined class.<br>
Example :
    ~~~Python
        class Employee:
            def __init__(self):
                self.name='Swati'
                self.salary=10000
            def __str__(self):
                return 'name='+self.name+'\n'+'salary=$'+str(self.salary)

        e = Employee()
        print(e)
    ~~~ 
    
7. The `__bool__` method takes one positional argument and returns either true or false. Its purpose is either to check an object is true or false, or to explicitly convert to a Boolean.