#to assign a "init" function to a class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is "+self.name)

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
p1.myfunc()

#Arbitrary Arguments, *args
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

#Arbitrary Keyword Arguments, **kwargs
def my_function1(**kid):
  print("His last name is " + kid["lname"])

my_function1(fname = "Tobias", lname = "Refsnes")