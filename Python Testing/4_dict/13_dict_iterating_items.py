d = {"Id": 1, "Name": "Kyaw Kyaw", "Position": "Developer", "Address": "Yangon", [100, 201, 301]: "Department Ids"}

for x, y in d.items():
    print(x, y)

# TypeError: unhashable type: 'list'
