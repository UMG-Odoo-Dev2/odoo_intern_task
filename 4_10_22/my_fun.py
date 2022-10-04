from decorator import do_twice

@do_twice
def say_whee():
    print("Whee!")
@do_twice
def greet(name):
    print(f"Hello {name}")
@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

say_whee()
greet("Wah Ko")
hi_adam = return_greeting("Adam")
print(hi_adam)

