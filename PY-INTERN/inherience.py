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
#Single-Inherience
class Developer(Person):
    def __init__(self,name,sex,profession,studytime,workhour):
        super().__init__(name,sex,profession,studytime)
        self.working_hour=workhour
    def working(self):
        print("My working hour is "+str(self.working_hour))
class Doctor(Person):
    def __init__(self,name,sex,profession,studytime,workhour,treat):
        super().__init__(name,sex,profession,studytime)
        self.treat=treat
    def treating(self):
        print("Treating")

#Multi-level Inherience
class Intern(Developer):
    pass
#Multiple-level Inherience
class Customer(Developer,Doctor):
    pass



p1=Developer("Wint Wah Ko","female","Odoo Developer",2,8)
p1.work()
p1.study()
p1.working()