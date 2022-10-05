from cmath import exp


class Example(object):
  
    # Initializing
    def __init__(self):
        print("Example Instance.")
  
    # Calling __delete__
    def __delete__(self, instance):
        print ("Deleted in Example object.")
  
# Creating object of Example
# class as an descriptor attribute
# of this class
class Foo(object):
    exp = Example()
    print(exp)
  
f = Foo()
print(f)
del f.exp

print(f)
print(f.exp)
