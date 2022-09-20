def myfun():
    print("This is First Function")
myfun()

def carfun(car):
    print(car + " On Fire")
carfun("Toyota")

def calFun(x,y):
    return x*y
print(calFun(4,8))

def multiFun(x,*y):
    print(x)
    print(y)
multiFun(3,5,2,6,3,6,8)

def starFun(fNum,**b):
    print(fNum)
    print(b)
starFun(fNum=8,secNum=34,thirdNum=22)


class Person:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
p = Person("Leo",27)
print(p.name)
print(p.age)
