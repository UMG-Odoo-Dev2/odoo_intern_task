l1=["blue","sky","orange","red","green","blue"]
l2=["blue","red","green"]
for element in l2:
    if element in l1:
        l1.remove(element)
 
print(l1)