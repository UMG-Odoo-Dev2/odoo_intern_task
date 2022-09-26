# **Mutable vs Immutable Objects in Python**
- Every variable in python holds an instance of an object. 
- There are two types of objects in python i.e. Mutable and Immutable objects.
### **Mutable**
- An object whose internal state can be changed is mutable
- These are of type list, dict, set . Custom classes are generally mutable.<br>
    `color = ["red", "blue", "green"]`
    `print(color)`<br>
    `color[0] = "pink"` <br>
    `color[-1] = "orange" `<br>
    `print(color)`<br>

- In this example , the contents of list are changed so that it is mutable.<br>
### **Immutable**
- An immutable doesn't allow any change in the object once it has been created.
- These are of in-built types like int, float, bool, string, unicode, tuple.

    #### **#Original String**
    `ori_str = "How are you! "`<br>
    `print("Original String: ","\n", ori_str)`<br>
    `print(id(ori_str),"\n")`<br>
    `print(type(ori_str))`<br>

    #### **#Add String**
    `add_str = ori_str + "Yes, I am"`<br>
    `print("Adding String:","\n",add_str)`<br>
    `print(id(add_str))`<br>
    `print(type(add_str),"\n")`<br>

    #### **#Replace String**
    `rpl_str = ori_str.replace("How","What")`<br>
    `print("Replacing String:","\n",rpl_str)`<br>
    `print(id(rpl_str))`<br>
    `print(type(rpl_str))`<br>
- In that examples , id of string is changed so this is immutable.
