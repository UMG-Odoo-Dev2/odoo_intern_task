origin_str="konnichiwa "
print(origin_str)
print(type(origin_str))
print(id(origin_str))

#Adding new data into an existing string
new_str= origin_str + "wah ko"
print(new_str)
print(id(new_str))
print(id(origin_str)==id(new_str))

#Replacing new data
replaced_str= origin_str.replace("konnichiwa","konbanwa")
print(replaced_str)
print(id(replaced_str))
print(id(origin_str)==id(replaced_str))