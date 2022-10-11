number_list=[1,2,3,4,5,6,7,8,9,10] 

new_list=list(filter(lambda x:(x%2==0),number_list))

print(new_list,type(new_list))

new_list=list(map(lambda x:pow(x,3),number_list))
print(new_list)

from functools import reduce
reduced=reduce(lambda x, y:x+y,number_list) #int type
print(reduced,type(reduced))


print(new_list)

new_list=list(map(lambda x:x*x,number_list))
print(new_list)

from functools import reduce
new_list=reduce(lambda x,y:x*y,number_list) #int type
print(new_list)
