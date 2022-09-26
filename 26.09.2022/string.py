from types import new_class


ori_str = "How are you! "
print("Original String: ","\n", ori_str)
print(id(ori_str),"\n")
print(type(ori_str))

# Add String
add_str = ori_str + "Yes, I am"
print("Adding String:","\n",add_str)
print(id(add_str))
print(type(add_str),"\n")

# Replace String
rpl_str = ori_str.replace("How","What")
print("Replacing String:","\n",rpl_str)
print(id(rpl_str))
print(type(rpl_str))


