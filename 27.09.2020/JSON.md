# **JSON (JavaScript Object Notatoin)**
- JSON is a syntax for storing and exchanging data.
- JSON is text, written with JavaScript object notation.
- Python has a built-in package called json, which can be used to work with JSON data.<br>

    Example : Import the json module
    
        ```import json```

### **Parse JSON - Convert from JSON to Python (Deserializing)**

- If you have a JSON string, you can parse it by using the json.loads() method.

    Example:

        import json

        # JSON String
        x =  '{ "name":"John", "age":30, "city":"New York"}'

        # parse x:
        y = json.loads(x)

        # the result is a Python dictionary:
        print(y["age"]) 
        print(type(y))
        # 30
        # <class dict> 

### **Convert from Python to JSON (Serializing)**

- If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

        Example:

        import json

        # a Python object (dict):
        x = {
        "name": "John",
        "age": 30,
        "city": "New York"
        }

        # convert into JSON:
        y = json.dumps(x)

        # the result is a JSON string:
        print(type(y)) 

        # <class str>

- to make it easier to read the result:<br>
    _Use the indent parameter to define the numbers of indents:_

        json.dumps(x, indent=4)
- to order the keys in the result:<br>
    _Use the sort_keys parameter to specify if the result should be sorted or not:_

        json.dumps(x, indent=4, sort_keys=True)