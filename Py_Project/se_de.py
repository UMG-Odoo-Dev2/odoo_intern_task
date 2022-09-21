#JSON to Python
import json
a='{"name":"Leo","age":"27","city":"Yangon"}'
b=json.loads(a)
print(b["city"],type(b))


#Python to JSON
x={"name":"Leo","age":"27","city":"Yangon"}
y=json.dumps(x,indent=2)
print(y,type(y))