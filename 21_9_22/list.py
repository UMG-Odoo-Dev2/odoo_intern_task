from tempfile import _TemporaryFileWrapper
from typing import Type


A=[1,2,3]
B=[3]
#C=[]
# for i in A:
#     if i not in B:
#         C.append(i)
#     else:
#         del(i)
# print (C)
print([i for i in A if i not in B])

