a=["orange","mango","grape","strawberry","banana","apple"]
b=["mango","grape","strawberry","cherry"]

c=list(set(a)-set(b))
print(c)

d=list(set(b)-set(a))
print(d)

c.extend(d)
print(c)