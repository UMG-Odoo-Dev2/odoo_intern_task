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