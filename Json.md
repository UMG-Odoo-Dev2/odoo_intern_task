## Python JSON
In this tutorial, you will learn to parse, read and write JSON in Python with the help of examples. Also, you will learn to convert JSON to dict and pretty print it.

<b>JSON (JavaScript Object Notation)</b> is a popular data format used for representing structured data. It's common to transmit and receive data between a server and web application in JSON format.

In Python, JSON exists as a string. For example:

    p = '{"name": "Bob", "languages": ["Python", "Java"]}'
It's also common to store a JSON object in a file.

## Import json Module
To work with JSON (string, or file containing JSON object), you can use Python's json module. You need to import the module before you can use it.

    import json
Parse JSON in Python
The json module makes it easy to parse JSON strings and files containing JSON object.

