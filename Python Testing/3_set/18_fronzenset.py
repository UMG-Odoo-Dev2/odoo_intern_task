fs = frozenset([1, 2, 3, 4, 5, 6, 7, 8])
print(type(fs))
for i in fs:
    print(i)
fs.remove(7)  # error
print(fs)
fs.add(9)  # error

# mutable = can add or remove
# immutable = cannot modified
