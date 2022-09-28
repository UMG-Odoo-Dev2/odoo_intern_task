# Reduce

from functools import reduce
pairs = [(1,'a'), (2,'b'), (3,'c')]
result = reduce(lambda acc, pairs: acc + pairs[0], pairs, 10) # sum 1st item of each pair
print(result,type(result))

rip =sum(x[0] for x in pairs)
print(rip,type(rip))

o = [3,4,7,2,8,9,10]
result1 = reduce(lambda x, y: x+y, o)
print(result1,type(result1))