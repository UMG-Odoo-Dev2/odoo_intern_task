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
- Json library exposes the dump() method for writing data to files. 
- There is also a dumps() method (pronounced as “dump-s”) for writing to a Python string.
- ***Note that*** dump() takes two positional arguments: (1) the data object to be serialized, and (2) the file-like object to which the bytes will be written.
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

## Deserializing JSON
- In the json library, load() and loads() for turning JSON encoded data into Python objects.
- Using a json.load() method, we can read JSON data from text, JSON, or binary file. 
- The json.load() method returns data in the form of a Python dictionary.
```
import json
print("Start to Read JSON file")
with open("developer.json", "r") as read_file:
    print("Converting JSON encoded data into Python dictionary")
    developer = json.load(read_file)

    print("Decod JSON Data From File")
    for key, value in developer.items():
        print(key, ":", value)
    print("Done reading json file")
```
- In this program, use the context manager, but this time you’ll open up the existing data_file.json in read mode.