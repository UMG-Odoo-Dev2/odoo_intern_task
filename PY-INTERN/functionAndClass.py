def print_fun():
    print ("Hello,This is print function")

print_fun()

def oneArg_fun(name):
    print("My name is "+name)
oneArg_fun("Wah Ko")

def twoArd_fun(a,b):
    if a<b:
        print (str(a)+" is less than "+str(b))
    elif a>b:
        print(str(a)+" is greater than "+str(b))
    else:
        print(str(a)+" is equal to "+str(b))
twoArd_fun(5,6)


def arbitaryArg_fun(name,*arg):
    print(name)
    print(arg,type(arg))
arbitaryArg_fun("mama","hlahla","myamya","koko","mgmg")

def kewordArg_fun(fletter,**kwa):
    print(fletter)
    print(kwa,type(kwa))
kewordArg_fun(fletter="hello",sletter="hi",tletter="hey",foletter="hola",filetter="konnichiha")

class Person:
    def __init__(self,name,sex,profession,studytime):
        self.name=name
        self.sex=sex
        self.profession=profession
        self.studytime=studytime
    
    def work(self):
        print(self.name,'work as ',self.profession)
    
    def study(self):
        print(self.name,'hours studies ',self.studytime,'a day')

p1=Person("Wint Wah Ko","female","Odoo Developer",2)
p1.work()
p1.study()


