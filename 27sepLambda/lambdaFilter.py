# Filter
even = lambda x : x%2 == 0
print(list(filter(even, range(11))))

list = [x for x in range(11) if x%2 == 0]
print(list, type(list))