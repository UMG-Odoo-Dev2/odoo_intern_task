# def check(args):
#     if(args % 3 == 0):
#         return True
#     else:
#         return False
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# for num in L:
#     if num % 3 == 0:
#         print(num)
# filtered = list(filter(check, L))
# print(filtered)
# for s in filtered:
#     print(s)
list_new = list(filter(lambda x:x % 3 == 0, L))
print(list_new)