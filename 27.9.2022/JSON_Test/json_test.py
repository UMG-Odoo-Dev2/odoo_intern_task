import json

print("Serialization:")
#dictionary
person_dict={
    'name':'Bob',
    'age': 12,
    'children':None
}

person_json=json.dumps(person_dict)

print(person_json)
print(type(person_json))

print("Deserialization:")
#JSON string
person='{"name": "Bob", "age": 12, "children": null}'

person_dict=json.loads(person)
print(person_dict)
print(type(person_dict))

print("Read JSON file:")
with open('person.json','r') as read_file:
    data=json.load(read_file)

print(data)
print(type(data))

print("Writing JSON into a file:")
person_dict={
    "name": "Bob", 
    "age": 12, 
    "children": None}

with open("person.txt","w") as write_file:
    json.dump(person_dict,write_file)

print("Pretty format:")
person_str='{"name": "Bob", "age": 12, "children": null}'
person_dict=json.loads(person_str)

print(json.dumps(person_dict,indent=4,sort_keys=True))
