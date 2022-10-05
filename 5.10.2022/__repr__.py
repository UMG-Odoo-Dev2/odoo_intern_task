class String:

    def __init__(self, str):
        self.str = str
    
    def __repr__(self):
        return 'Object: {}'.format(self.str)
  
if __name__ == '__main__':
    string1 = String('Hello')
    print(string1)