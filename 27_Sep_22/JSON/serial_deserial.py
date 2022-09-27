import json
# JSON string
employee = '{"id":"05", "name": "MayPhyoThu", "department":"CID"}'

# Convert string to Python dict (Deserialization)
employee_dict = json.loads(employee)
print(employee_dict)
print(type(employee_dict))
print("\n")


# Convert Python dict to JSON (Serialization)
json_object = json.dumps(employee_dict, indent=8)
print(json_object)
print(type(json_object))

