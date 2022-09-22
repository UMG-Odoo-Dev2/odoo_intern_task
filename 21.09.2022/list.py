a=["orange","mango","grape","strawberry","banana","apple"]
b=["mango","grape","strawberry","cherry"]

c=list(set(a)-set(b))
print(c)
d=list(set(b)-set(a))
print(d)

c.extend(d)
print(c)

#c=list(set(a)-set(b))

# for fruit in a:
#       if fruit in b:
#           b.remove(fruit)
# new_list = []
# new_list( a.extend(b))

# print(new_list)






# l = [1, 2, 4, 2, 1, 4, 5]
# print("Original List: ", l)
# res = [*set(l)]
# print("List after removing duplicate elements: ", res)


