or_string="Where are you from?"

print("Original String: ")
print(or_string)  #content
print(id(or_string))   #memory address
print(type(or_string),"\n") #type

#adding
add_string=or_string+" I live in Yangon."

print("Added String: ")
print(add_string)
print(id(add_string))
print(type(add_string),"\n")

#replacing
re_string=or_string.replace("are","do").replace("from","come from")

print("Replacing: ")
print(re_string)
print(id(re_string))
print(type(re_string),"\n")


my_list=[1,2,3,4,5,6,7,8]
sec_list=[9,10]
#append_list=my_list.append(sec_list)
print(my_list)
print(id(my_list))
print(type(my_list),"\n")

my_list.extend(sec_list)
print(my_list)
print(id(my_list))
print(type(my_list))


