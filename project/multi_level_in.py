class Person:
    def eat(self):
        print("I am eating")

    def drink(self):
        print("I am drinkig")
p=Person()
p.drink()
p.eat()

class Father (Person):
    def myfun(self):
        print("I live in Yangon")
f = Father()
f.myfun()
f.drink()
f.eat()


class Son (Father):
    def doc(self):
        print("I am a doctor")
s=Son()
s.doc()
s.myfun()
s.drink()
s.eat()