# Objects Explanation in Python

- In Python, everything is treated as an object
- Every object has these three characteristics:
    * identity: address that the object refers to in the computer's memory
    * type: kind of object that is created
    * value: value(content) stored by the object
- Mutable: an object whose internal state can be changed
- Eg. lists, sets, dictionaries, etc.
- Immutable: an object doesn't allow any change once it has been created
- Eg. numbers (integer, float, etc.), strings, tuples, etc.
<<<<<<< HEAD
```py
=======
```
>>>>>>> 0c915ca04e9305325e7bfae7d98aa8e46be9f264
string="Where are you from?"

print("Original String: ")
print(string)  #content
print(id(string))   #memory address
print(type(string),"\n") #type

#adding
add_string=string+" I live in Yangon."

print("Added String: ")
print(add_string)
print(id(add_string))
print(type(add_string),"\n")

#replacing
re_string=string.replace("are","do").replace("from","come from")

print(re_string)
print(id(re_string))
print(type(re_string),"\n")
```
 *Code Explanation-1*

 - First, a string (or_string) is created.
 - And then, print characteristics (id, type and content) of the original string
 - after adding or replacing the string, print characteristics of added or replaced string
 - ID of these strings are different.
 - Original string cannot be changed because a string object is immutable.

<<<<<<< HEAD
 ```py
=======
 ```
>>>>>>> 0c915ca04e9305325e7bfae7d98aa8e46be9f264
 my_list=[1,2,3,4,5,6,7,8]
 sec_list=[9,10]
 
 print(my_list)
 print(id(my_list))
 print(type(my_list),"\n")

 my_list.extend(sec_list)
 print(my_list)
 print(id(my_list))
 print(type(my_list))
 ```
 *Code Explanation-2*
 
 - First, two lists(my_list and sec_list) are created.
 my_list is a original list and sec_list is a list for adding in my_list.
 - And then, print characteristics (id, type and content) of the original list.
 - after extending the list, print characteristics of extended list
 - ID of two lists are the same.
 - Original list can be changed because a list object is mutable.


