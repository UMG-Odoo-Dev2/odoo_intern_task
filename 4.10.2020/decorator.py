from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 8:
            func()
        else:
            pass  # Hush, the neighbors are asleep
            print("pass")
    return wrapper

def say_whee():
    print("Whee!")

a = not_during_the_night(say_whee)
a()


