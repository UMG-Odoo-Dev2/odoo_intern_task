#One Arg
whating = lambda x : x-5
print(whating(27))

#Two Arguments
multiply = lambda a,b : a*b
print(multiply(5,8))

#Multi Arguments
student = lambda name, age, major : f'Name : {name}, Age : {age}, Major : {major}'
print(student("Leo","27","CS"))

#One Line Lambda
print((lambda p, q, r : q + q + r)(13,25,18))

#Filter in Lambda
karma = list(filter(lambda w : 'K' in w, ["Kilo","Milo","Pilo"]))
print(karma)

#How to merge two dicts 
m = {'a': 1 , 'b': 2}
n = {'b': 3 , 'c': 4}
o = {**m, **n}
print(o,type(o))

#High Order Functon
high_ord = lambda x, func : x + func(x)
print(high_ord(2, lambda x: x * 3))