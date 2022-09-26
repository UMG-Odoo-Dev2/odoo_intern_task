str ="I am learning Python"
print("Original String: ")
print(str)  #content
print(id(str))   #memory address
print(type(str)) #type

#adding
add_str=str +",I am really enjoy the python programming language!"

print("\n Adding String: ")
print(add_str)
print(id(add_str))
print(type(add_str))

#replacing
replace_str=add_str.replace("I","We").replace("am","are").replace("python","ruby")

print("\n Replacing: ")
print(replace_str)
print(id(replace_str))
print(type(replace_str),"\n")


list_A=[5,10,15,20,25,30,35]
list_B=[100,200]

print(list_A)
print(id(list_A))
print(type(list_A),"\n")

#append_list=list_A.append(list_B)
list_A.extend(list_B)
print(list_A)
print(id(list_A))
print(type(list_A),"\n")

# (Output)
# Original String: 
# I am learning Python
# 2005534765184
# <class 'str'>

#  Adding String:
# I am learning Python,I am really enjoy the python programming language!
# 2005534874672
# <class 'str'>

#  Replacing:
# We are learning Python,We are really enjoy the ruby prograreming language!
# 2005534874544
# <class 'str'>

# [5, 10, 15, 20, 25, 30, 35]
# 2005534777984
# <class 'list'>

# [5, 10, 15, 20, 25, 30, 35, 100, 200]
# 2005534777984
# <class 'list'>

tup1 = ('apple', 'banana',[5,4,3,2,1]) 
tup2 = ('apple', 'banana',[5,4,3,2,1])
print(tup1==tup2) #True
print(tup1 is tup2) #False
tup1[2].append(90)
print(tup1)
print(tup1==tup2) #False