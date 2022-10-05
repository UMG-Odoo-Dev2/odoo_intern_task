
class Employee:
    def __init__(self):
        self.name='Swati'
        self.salary=10000
    def __str__(self):
        return 'name='+self.name+'\n'+'salary=$'+str(self.salary)

e = Employee()
print(e)