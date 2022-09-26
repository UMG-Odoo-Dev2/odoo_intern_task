# def remove(a, b):
#     a, b = [i for i in a if i not in b],[j for j in b if j not in a]
#     print("list1 : ", a)
#     print("list2 : ", b)
#     print("list3 : ", a+b)
# if __name__ == "__main__":
#     a = [1, 2, 3, 4, 5]
#     b = [4, 5, 6, 7, 8]
# remove(a, b)

list_A = [1, 3, 4, 6, 7]
list_B = [3, 6]
 
#list_C= [i for i in list_A if i not in list_B]

c = list(set(list_A)-set(list_B))

#print ("After remove  : " + str(list_C))
print(c)