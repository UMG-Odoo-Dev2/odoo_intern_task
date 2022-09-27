import json

person_dict={'name':'Bob','age': 12,'children':None} #dict

person_json=json.dumps(person_dict)

print(person_json)
print(type(person_json)) #<class str> (object form)

person_list=["name","Bob","age",12] #list
person_json=json.dumps(person_list)

print(person_json)
print(type(person_json)) #<class str> (array form)

person_tuple=("name","Bob","age",12) #tuple
person_json=json.dumps(person_tuple)

print(person_json)
print(type(person_json)) #<class str> (array form)

person_str="His name is Bob."
person_json=json.dumps(person_str)#str

print(person_json)
print(type(person_json)) #<class str> (string form)

int_num=12
person_json=json.dumps(int_num)#int

print(person_json)
print(type(person_json)) #<class str> (number form)

float_num=12.0
person_json=json.dumps(float_num)#float

print(person_json)
print(type(person_json)) #<class str> (number form)

bool_test=True
person_json=json.dumps(bool_test)#True / False

print(person_json)
print(type(person_json)) #<class str> (true)

null_test=None
person_json=json.dumps(null_test)#None

print(person_json)
print(type(person_json)) #<class str> (Null)

person={"name":"John","age":40,"Married":True,"nationality":"American","children":("Jenny","Rose"),"pets":None}

print(json.dumps(person))
print(json.dumps(person,indent=0))
print(json.dumps(person,indent=1))
print(json.dumps(person,indent=2))
print(json.dumps(person,indent=-1))

print(json.dumps(person,indent=4,sort_keys=True))

print(json.dumps(person,indent=4,sort_keys=True,separators=(".","=")))

