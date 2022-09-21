# addition = lambda x,y : x + y
# print(addition(2,3))


# people =lambda name,gender,age: f'Name:{name} Gender:{gender} Age:{age}'
# print(people("wahko","female",22))


# print((lambda x,y:x*y)(3,4))


# numbers=[1,2,3,4,5,6,7,34,57,69,13,21,20]
# filtered_numbers=list(filter(lambda x: x%2==0,numbers))
# print(filtered_numbers)

# mapped_list=list(map(lambda x: x.upper(), ['cat', 'dog', 'cow']))
# print(mapped_list)

from functools import reduce

no_map=lambda a:a*2
print(no_map([1,2,3]))

map_list= list(map(lambda b:b*2,[1,2,3]))
print(map_list)


before_reduce=[1,2,3,4,5,6,7,8,9]
after_reduce=reduce(lambda x,y: x+y,before_reduce)
print(after_reduce)