lst1 = [1,2,3,4,5,6,7,8,9]
lst2 = [4,5,6]
def intersection(lst1,lst2):
    return list(set(lst1)&set(lst2)) 
print(intersection(lst1,lst2))
#new_list=list(filter(lambda x: intersection(lst1,lst2))
#print(new_list)