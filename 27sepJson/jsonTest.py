import json

# Python to JSON (Serialization)
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}
result = json.dumps(data, indent=4) # Use json.dumps() instead. json.dump() needs a file object and dump JSON to it
print(result)


# JSON to Python (Deserialization)
deserial = '{"name":"Leo","age":27,"job":"Office Staff"}'
pyResult = json.loads(deserial)
print(pyResult)