a = [1,2,3,4,5,6]
b = [1,2,3,8]
# for c in b:
#     print(c, type(c))
#     if c in a:
#         a.remove(c)

# print(a, type(a))
# print(c, type(c))
c = list(set(a)- set(b))
print(c)