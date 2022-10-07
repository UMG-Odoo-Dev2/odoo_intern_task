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