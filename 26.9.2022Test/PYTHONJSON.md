# PYTHON JSON
- JSON is a syntax for storing and exchanging data.

- JSON is text, written with JavaScript object notation.

## JSON in Python
Python has a built-in package called json, which can be used to work with JSON data.
```bash
Example
Import the json module:

    import json 
```
## Parse JSON - Convert from JSON to Python

If you have a JSON string, you can parse it by using the json.loads() method.
```bash
Example
Convert from JSON to Python:

    import json
    x =  '{ "name":"John", "age":30, "city":"New York"}'
    y = json.loads(x)
    print(y["age"])


output:30
```
## Convert from Python to JSON
If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
```bash
Example

Convert from Python to JSON:
import json


    x = {
      "name": "John",
      "age": 30,
      "city": "New York"
    }
    y = json.dumps(x)
    print(y) 

Output:  {"name": "John", "age": 30, "city": "New York"}
```

## We can convert Python objects of the following types, into JSON strings:

- dict
- list
- tuple
- string
- int
- float
- True
- False
- None
```bash
Example

Convert Python objects into JSON strings, and print the values:

    import json

    print(json.dumps({"name": "John", "age": 30}))
    print(json.dumps(["apple", "bananas"]))
    print(json.dumps(("apple", "bananas")))
    print(json.dumps("hello"))
    print(json.dumps(42))
    print(json.dumps(31.76))
    print(json.dumps(True))
    print(json.dumps(False))
    print(json.dumps(None)) 

Output:{"name": "John", "age": 30}
["apple", "bananas"]
["apple", "bananas"]
"hello"
42
31.76
true
false
null 
```
## When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:
Python To JSON
- dict TO	Object
- list To	Array
- tuple To	Array
- str To	String
- int To	Number
- float To	Number
- True To	true
- False To	false
- None To	null

```bash
Example

Convert a Python object containing all the legal data types:

    import json

    x = {
        "name": "John",
        "age": 30,
        "married": True,
        "divorced": False,
        "children": ("Ann","Billy"),
        "pets": None,
        "cars": [
            {"model": "BMW 230", "mpg": 27.5},
            {"model": "Ford Edge", "mpg": 24.1}
        ]
    }

    print(json.dumps(x))

Output:{"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann","Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]} 
```
## Format the Result

The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.

The json.dumps() method has parameters to make it easier to read the result:
```bash
Example

Use the indent parameter to define the numbers of indents:

    import json

    x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann","Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
    }
    print(json.dumps(x, indent=4))

Output:{
    "name": "John",
    "age": 30,
    "married": true,
    "divorced": false,
    "children": [
        "Ann",
        "Billy"
    ],
    "pets": null,
    "cars": [
        {
            "model": "BMW 230",
            "mpg": 27.5
        },
        {
            "model": "Ford Edge",
            "mpg": 24.1
        }
    ]
} 
```
You can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:
```bash
Example

Use the separators parameter to change the default separator:

    import json

    x = {
        "name": "John",
        "age": 30,
        "married": True,
        "divorced": False,
        "children": ("Ann","Billy"),
        "pets": None,
        "cars": [
            {"model": "BMW 230", "mpg": 27.5},
            {"model": "Ford Edge", "mpg": 24.1}
        ]
        }
    print(json.dumps(x, indent=4, separators=(". ", " = ")))

Output:{
    "name" = "John".
    "age" = 30.
    "married" = true.
    "divorced" = false.
    "children" = [
        "Ann".
        "Billy"
    ].
    "pets" = null.
    "cars" = [
        {
            "model" = "BMW 230".
            "mpg" = 27.5
        }.
        {
            "model" = "Ford Edge".
            "mpg" = 24.1
        }
    ]
} 
```
## Order the Result

The json.dumps() method has parameters to order the keys in the result:
```bash
Example

Use the sort_keys parameter to specify if the result should be sorted or not:

    import json

    x = {
        "name": "John",
        "age": 30,
        "married": True,
        "divorced": False,
        "children": ("Ann","Billy"),
        "pets": None,
        "cars": [
            {"model": "BMW 230", "mpg": 27.5},
            {"model": "Ford Edge", "mpg": 24.1}
        ]
        }
    print(json.dumps(x, indent=4, sort_keys=True))

Output:{
    "age": 30,
    "cars": [
        {
            "model": "BMW 230",
            "mpg": 27.5
        },
        {
            "model": "Ford Edge",
            "mpg": 24.1
        }
    ],
    "children": [
        "Ann",
        "Billy"
    ],
    "divorced": false,
    "married": true,
    "name": "John",
    "pets": null
} 






