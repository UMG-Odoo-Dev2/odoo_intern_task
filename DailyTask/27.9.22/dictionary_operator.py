from filecmp import cmp
from msilib import sequence

d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"hello": 7, "world":5, "my": 6}

# print(d1 * 2) TypeError: unsupported operand type(s) for *: 'dict' and 'int'
# print(d1+d2) TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
print("a" in d1)
# d3 = cmp(d1, d2)
# print(d3) #TypeError: stat: path should be string, bytes, os.PathLike or integer, not dict

print(len(d1))
print(max(d2))
print(min(d2))
print(d2(sequence)) #TypeError: 'dict' object is not callable