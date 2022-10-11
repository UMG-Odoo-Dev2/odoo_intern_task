# JSON
- JavaScript Object Notation
- a popular data format used for representing structured data
- It's common to transmit and receive data between a server and web applications in JSON format
- JSON supports primitive types, like string and number, as well as nested lists and objects
- In Python, JSON exists as a string

```
person='{"name": "Bob", "age": 12, "children": null}'
```
- Python comes with a built-in package called *json* for encoding and decoding JSON data
- *Serialization*: process of encoding JSON (transformation of data into a series of bytes to be stored or transmitted across a network)
- *Deserialization*: process of decoding data that has been stored or delivered in the JSON format
- To work with JSON (string or file containing JSON object), need to import JSON module before using it
```
import json
```
### Serializing JSON (Convert from Python to JSON)

```
import json

peron_dict={
    'name':'Bob',
    'age': 12,
    'children':None
}
person_json=json.dumps(person_dict)
print(person_json)
print(type(person_json))

#output
{"name": "Bob", "age": 12, "children": null}
<class 'str'>
```
Here, `person_dict` is a dictionary and `person_json` is a JSON string.
### Deserializing JSON (Convert from JSON to Python)
```
import json

person='{"name": "Bob", "age": 12, "children": null}'

person_dict=json.loads(person)
print(person_dict)
print(type(person_dict))

#output
{'name': 'Bob', 'age': 12, 'children': None}
<class 'dict'>
```
Here, `person` is a JSON string and `person_dict` is a dictionary.

### Reading JSON file
```
person.json

{"name": "Bob", "age": 12, "children": null}

json_test.py

import json

with open('person.json','r') as read_file:
    data=json.load(read_file)

print(data)
print(type(data))

#output
{'name': 'Bob', 'age': 12, 'children': None}
<class 'dict'>
```
Here, JSON file is read using `open()` function and parsed using `json.load( )` method which gives as a dictionary named `data`
### Writing JSON into a file
```
json_test.py

person_dict={
    "name": "Bob", 
    "age": 12, 
    "children": None
}

with open("person.txt","w") as write_file:
    json.dump(person_dict,write_file)

person.txt
{"name": "Bob", "languages": ["Java", "Python"]}
```
Here, a file (`person.txt`) is opened in writing mode using `w`. If the file doesn't already exist, it will be created. Then, `json.dump()` transforms `person_dict` to a JSON string which will be saved in the `person.txt` file

- To analyze and debug JSON data, need to print it in a more readable format by passing additional parameters `indent` and `sort_keys` to `json.dump()` and `json.dumps()` method.
```
import json

person_str='{"name": "Bob", "age": 12, "children": null}'
person_dict=json.loads(person_str)

print(json.dumps(person_dict,indent=4,sort_keys=True))

#output
{
    "age": 12,
    "children": null,
    "name": "Bob"
}
```
- 4 spaces are used for indentation and the keys are sorted in ascending order.
- the default value of `indent` is `None` and of `sort_keys` is `False`.