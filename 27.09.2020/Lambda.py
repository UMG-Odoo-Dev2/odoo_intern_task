# Map()
# x=tuple(map(lambda x: x.capitalize(), ['cat', 'dog', 'cow']))
# print(x)

# y=map(lambda x: x.capitalize(), ('cat', 'dog', 'cow'))
# print(y)

# Filter()
even = lambda x: x%2 == 0
even=list(filter(even, range(11)))
print(even)

odd = lambda x: x%2 !=0
odd = tuple(filter(odd,range(15)))
print(odd)


# Reduce()
import functools
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
z=functools.reduce(lambda acc, pair: acc + pair[0], pairs, 1)
print(z)

pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
result=sum(x for x, _ in pairs)
print(result)


