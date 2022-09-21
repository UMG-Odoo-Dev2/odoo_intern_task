# x=lambda a:a+10
# print(x(5))       #15

# y=lambda a,b:a*b
# print(y(5,2))     #10      

# def myfun(n):
#     return lambda a:a*n   
# mydoubler=myfun(2)    
# mytripler=myfun(3)
# print(mydoubler(10))  #20
# print(mytripler(10))  #30

# y=(lambda x: x + 1)(2)
# print(y)                  #3

#print((lambda x, y: x+y)(2,3)) #5

#y=lambda x: x + 1
#print(y(2))    #3

#full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
#print(full_name('guido','van rossum')) # Full name: guido van rossum

# full_name = lambda first, last:dir(first) # last
# print(full_name('guido','van rossum')) 

high_ord_func = lambda x, func: x + func(x)
print(high_ord_func(2, lambda x: x * x))

print(high_ord_func(2, lambda x: x + 3))
