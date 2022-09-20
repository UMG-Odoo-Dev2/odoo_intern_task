import json
p={"name":"wah ko","age":22,"salary":200000}
j=json.dumps(p)
print(j,type(j))

j1='{"name":"wah ko","age":22,"salary":200000}'
p1=json.loads(j1)
print(p1,type(p1))