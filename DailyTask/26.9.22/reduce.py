import functools
 
lis = [5, 3, 4, 6, 1, 7, 3, 2 ]
 
print(functools.reduce(lambda a, b: a+b, lis))
 
print(functools.reduce(lambda a, b: a if a > b else b, lis))