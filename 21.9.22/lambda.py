list1 = [1,2,4,6,7,8,9,10]
list2 = filter (lambda x: x > 4, list1) 
print(list(list2))                         #output=[6, 7, 8, 9, 10]

list_A = [10,2,8,7,5,4,3,11,0, 1]
list_B = map (lambda x: x*x, list_A) 
print(list(list_B))                        #output=[100, 4, 64, 49, 25, 16, 9, 121, 0, 1]

map_list=list(map (lambda x:x.upper(),["Python","Php","Odoo","JavaScript"]))
print(map_list)                            #output=['PYTHON', 'PHP', 'ODOO', 'JAVASCRIPT']

from functools import reduce
sequences = [1,2,3,4,5]
product = reduce (lambda x, y: x*y, sequences)
print(product)                             #output=120
