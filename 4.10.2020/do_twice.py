
from reusing_decorator import do_twice

@do_twice
def say_whee():
    print("Whee!")
# say_whee = do_twice(say_whee)
@do_twice
def greet(name): 
    print(f"Hello {name}")

say_whee()
greet("BOB") # wrapper_do_twice() takes 0 positional arguments but 1 was given
