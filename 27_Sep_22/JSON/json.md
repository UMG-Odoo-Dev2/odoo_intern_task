# JSON
> JavaScript Object Notation
- It was inspired by a subset of the JavaScript programming language dealing with object literal syntax.
- It is a format for structuring data.
- It is mainly used for storing and transferring data between the browser and the server. 
- Python too supports JSON with a built-in package called json. 
```
import json
```
- This package provides all the necessary tools for working with JSON Objects including parsing, serializing, deserializing, and many more.
- The process of encoding JSON is usually called <span style="color:green;font-weight:700;font-size:15px">serialization</span>
- <span style="color:green;font-weight:700;font-size:15px">Deserialization</span> is the reciprocal process of decoding data that has been stored or delivered in the JSON standard.

## Serializing JSON
- It needs to take a data dump.
- The json.dump() method (without “s” in “dump”) used to write Python serialized object as JSON formatted data into a file.
- The json.dumps() method encodes any Python object into JSON formatted String.
- Serialization Example: json.dump() to encode and write JSON data to a file
```
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)
```
- Using Python’s context manager, you can create a file called data_file.json and open it in write mode. (JSON files conveniently end in a .json extension.)

- *** Serialization Example: Convert Python dictionary into a JSON formatted String by using json.dumps() ***
```
import json

def SendJsonResponse(resultDict):
    print("Convert Python dictionary into JSON formatted String")
    developer_str = json.dumps(resultDict)
    print(developer_str)

# sample developer dict
developer_Dict = {
    "name": "Jane Doe",
    "salary": 9000,
    "skills": ["Python", "Machine Learning", "Web Development"],
    "email": "jane.doe@pynative.com"
}
SendJsonResponse(developer_Dict)
``` 
- Output is:
```
Writing JSON data into a Python String
{"name": "Jane Doe", "salary": 9000, "skills": ["Python", "Machine Learning", "Web Development"], "email": "jane.doe@pynative.com"}
```
- In this program, json.dumps() returns the JSON string representation of the Python dict.


- The json.dump() and  json.dumps()  is used for following operations
    - Encode Python serialized objects as JSON formatted data.
    - Encode and write Python objects into a JSON file
    - PrettyPrinted JSON data
    - Skip nonbasic types while JSON encoding
    - Perform compact encoding to save file space
    - Handle non-ASCII data while encoding JSON

## Deserializing JSON
- In the json library, load() and loads() for turning JSON encoded data into Python objects.
- Using a json.load() method, we can read JSON data from text, JSON, or binary file. 
- The json.load() method returns data in the form of a Python dictionary.
> ***Note that*** 
- To parse JSON from URL or file, use <span style="color:green;font-weight:700;font-size:15px">json.load().</span>
- For parse string with JSON content, use <span style="color:green;font-weight:700;font-size:15px">json.loads().</span>

- Example:***json.load() to read JSON data from a file and convert it into a dictionary***
```
import json
print("Start to Read JSON file")
with open("developer.json", "r") as read_file:
    print("Converting JSON encoded data into Python dictionary")
    developer = json.load(read_file)

    print("Decode JSON Data From File")
    for key, value in developer.items():
        print(key, ":", value)
    print("Done reading json file")
```
- In this program, use the context manager, but this time you’ll open up the existing developer_file.json in read mode.

- Another Example:***json.loads() to convert JSON string to a dictionary***
```
import json
employee = '{"id":"05", "name": "MayPhyoThu", "department":"CID"}'   ***this is JSON string***

***Convert string to Python dict (Deserialization)***
employee_dict = json.loads(employee)
print(employee_dict)
print(type(employee_dict))
print("\n")
```
- In this example, by using json.loads() method, we can deserialize native String, byte, or bytearray instance containing a JSON document to a Python dictionary.
