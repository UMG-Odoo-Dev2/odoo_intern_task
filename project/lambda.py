from time import process_time_ns


x=lambda a:a+10
print(x(5))

y=lambda a,b:a*b
print(y(5,2))

def myfun(n):
    return lambda a:a*n

mydoubler=myfun(2)
mytripler=myfun(3)
print(mydoubler(10))
print(mytripler(10))