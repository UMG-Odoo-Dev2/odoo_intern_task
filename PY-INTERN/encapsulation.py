class Person:
    def __init__(self):
        self._id=10
        
class Employee(Person):
    def __init__(self,name,salary):
        Person.__init__(self)
        self.name=name
        self.salary=salary

    def print_fun(self):
        print("Name: ",self.name, "Salary: ",self.salary)

emp1=Employee("Yuki",200000)
emp1.print_fun()
print("Employee's name: ",emp1.name) #public access
print("Employee's id: ",emp1._id)#protected access

