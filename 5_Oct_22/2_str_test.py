#Example2:
class Employee:
    def __init__(self):
        self.name='May Phyo'
        self.salary=10000
    def __str__(self):
        return 'name='+self.name+' salary=$'+str(self.salary)
e1=Employee()
print(e1)