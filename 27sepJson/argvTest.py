import sys
print("This is the name of the program: ", sys.argv[0])
print("Number of elements including the name of the program:",
       len(sys.argv))
print("Number of elements excluding the name of the program:",
      (len(sys.argv)-3))
print("Argument List: ", str(sys.argv))


add = 0.0
n = len(sys.argv)
for i in range(1, n): # range 0 is fileName, so start from 1
    add += float(sys.argv[i])
print(add,type(add))