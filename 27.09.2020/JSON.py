# import json
# json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])

# # print(json.dumps("\"foo\bar"))

# # print(json.dumps('\u1234'))

# # print(json.dumps('\\'))

# # print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))


# # from io import StringIO
# # io = StringIO()
# # json.dump(['streaming API'], io)
# # io.getvalue()
# # '["streaming API"]'

import json
from textwrap import indent
# x =  '{ "name":"John", "age":30, "city":"New York"}'
# y = json.loads(x)
# print(y["age"]) 
# print(type(y))

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
#y = json.dumps(x)
y = json.dumps(x)
print(y)
print(type(y))


print(function.__defaults__(indent))


