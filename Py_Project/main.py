import json
#some JSON
x='{"name":"Leo","age":"27","city":"Yangon"}'
#parse x
y=json.loads(x)
#The result is a python Dict
print(y["city"])
