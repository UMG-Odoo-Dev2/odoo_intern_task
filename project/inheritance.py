class Person:
    def eat(self):
        print("Person is eating")

    def drink(self):
        print("Person is drinkig")

class Student (Person):
    def myfun(self):
        print("I am a Student")
std = Student()
std.drink()
std.myfun()

class Doctor (Person):
    def doc(self):
        print("I am a doctor")
d=Doctor()
d.doc()
d.drink()
d.eat()

