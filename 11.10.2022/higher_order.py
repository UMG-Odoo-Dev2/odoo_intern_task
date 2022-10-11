def odd_or_even(num):
    if (num % 2) == 0:
        return "even"
    else:
        return "odd"

def higher_order_function(func,number):
    confirm=func(number)
    return confirm

num=int(input("Is this number odd or even?\n"))
result=higher_order_function(odd_or_even,num)
print(num," is a ",result," number")


or_list=[1,2,3,4,5]
def cube(n):
    return n**3

cube_list=map(cube,or_list)
print(list(cube_list))

lcube_list=map(lambda n:n**3,or_list)
print(list(lcube_list))

# lis=filter(cube,or_list)
# print(list(lis))

num_list=[1,2,3,4,5]
def is_odd(n):
    if(n%2!=0):
        return True
    else:
        return False

odd_list=filter(is_odd,num_list)
print(list(odd_list))

lodd_list=filter(lambda n:(n%2)!=0,num_list)
print(list(lodd_list))

org_list=[1,2,3,4,5]
def is_sum(x,y):
    return x+y

from functools import reduce
sum=reduce(is_sum,org_list)
print(sum)

import functools
lsum=functools.reduce(lambda x,y:x+y,org_list)
print(lsum)