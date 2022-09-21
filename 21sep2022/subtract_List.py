list1 = [8,7,6,9,5,4]
list2 = [5,4,7]

#print([i for i in list1 if i not in list2])

resultList = list(set(list1) - set(list2))
print(resultList,type(resultList))