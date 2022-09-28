# Map

result = list(map(lambda x : x.capitalize(), ['me','you','mood']))
print(result,type(result))

li = [2,5,9,8,7,3,6]
result = list(map(lambda x: x+x, li))
print(result,type(result))