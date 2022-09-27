# JSON
- JSON is a syntax for storing and exchanging data<br>
- JSON is text, written with JavaScript object notation

Python has a built-in package called json, which can be used to work with JSON data.<br>

Import the json module:

    import json

## Convert from JSON to Python

    import json

    # some JSON:
    x =  '{ "name":"John", "age":30, "city":"New York"}'

    # parse x:
    y = json.loads(x)

    # the result is a Python dictionary:
    print(y["age"])

## Convert from Python to JSON

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
    print(y)


The json.dumps() method has parameter called indent to make it easier to read the result.<br>

Use the indent parameter to define the numbers of indents:

    json.dumps(x, indent=4)

The json.dumps() method has separators, default value is (", ", ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values.<br>

Use the separators parameter to change the default separator:

    json.dumps(x, indent=4, separators=(". ", " = "))

Use the sort_keys parameter to specify if the result should be sorted or not:

    json.dumps(x, indent=4, sort_keys=True)
