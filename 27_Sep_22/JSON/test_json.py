import json

print("Start to Read JSON file")
with open("developer.json", "r") as read_file:
    print("Converting JSON encoded data into Python dictionary")
    developer = json.load(read_file)

    print("Decod JSON Data From File")
    for key, value in developer.items():
        print(key, ":", value)
    print("Done reading json file")

#Access JSON data directly using key name
print("\nStarted Reading JSON file")
with open("developer.json", "r") as read_file1:
    print("Converting JSON encoded data into Python dictionary")
    developer1 = json.load(read_file1)

    print("Decoding JSON Data From File")
    print("Printing JSON values using key")
    print(developer1["name"])
    print(developer1["salary"])
    print(developer1["skills"])
    print(developer1["email"])
    print("Done reading json file")



# json.loads() to convert JSON string to a dictionary
developerJsonString = """{
    "name": "jane doe",
    "salary": 9000,
    "skills": [
        "Raspberry pi",
        "Machine Learning",
        "Web Development"
    ],
    "email": "JaneDoe@pynative.com",
    "projects": [
        "Python Data Mining",
        "Python Data Science"
    ]
}
"""

print("Started converting JSON string document to Python dictionary")
developerDict = json.loads(developerJsonString)

print("Printing key and value")
print(developerDict["name"])
print(developerDict["salary"])
print(developerDict["skills"])
print(developerDict["email"])
print(developerDict["projects"])
print("Done converting JSON string document to a dictionary")


#Parse and Retrieve nested JSON array key-values
developerInfo = """{
    "id": 23,
    "name": "jane doe",
    "salary": 9000,
    "email": "JaneDoe@pynative.com",
    "experience": {"python":5, "data Science":2},
    "projectinfo": [{"id":100, "name":"Data Mining"}]
}
"""
print("\nStarted reading nested JSON array")
developerDict = json.loads(developerInfo)

print("Project name: ", developerDict["projectinfo"][0]["name"])
print("Experience: ", developerDict["experience"]["python"])

print("Done reading nested JSON Array")

#Serialization Example:
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)


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
