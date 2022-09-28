# JSON in Python
> JSON (JavaScript Object Notation)

- Based on JavaScript object
- We use JSON to store and exchange data
- Exists as its own standard
- Easy for both humans and machines to create and understand
- JSON is supposed to be readable by anyone who’s used a C-style language

> JSON Data Type

- Although JSON is created based on JavaScript's Object,
data type can not use like JavaScript.
### Valid Data Type on JSON
   - `Object, Array, String, Number, true, false, null`

### Invalid Data Type on JSON
   - `Function, Date, Undefined`

- JSON can be object or array

> Python supports JSON Natively!

### Convert from JSON to Python (Deserialization)

- eg code

```
# Some JSON
deserial = '{"name":"Leo","age":27,"job":"Office Staff"}'
pyResult = json.loads(deserial)
print(pyResult)
```
- Output (Python Dictionary)

```
{'name': 'Leo', 'age': 27, 'job': 'Office Staff'}
```

### Convert Python to JSON (Serialization)

- eg code

```
# Python Dictionary
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}
result = json.dumps(data, indent=4)
print(result)
```
- Output (JSON String)

```
{
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}
```


