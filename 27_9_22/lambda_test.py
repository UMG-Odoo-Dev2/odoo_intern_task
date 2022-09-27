# Map
map_list= list(map(lambda x: x.capitalize(), ['cat', 'dog', 'cow']))
print(map_list)

# Filter
odd =lambda x:x%2 != 0
filter_list= list(filter(odd,range(11)))
print(filter_list)

# Reduce
import functools
pairs = [(1, 3), (2, 4), (3, 5)]
reduced_result=functools.reduce(lambda acc, pair: acc + pair[0], pairs,0)
print(reduced_result)