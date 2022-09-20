# Function Calling
#  def my_function():
#   print("Hello from a function")

#  my_function()

# Arguments
# def my_function(fname):
#   print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus") 

# Arguments or parameters
#def my_function(fname, lname):
 # print(fname + " " + lname)

#my_function("Emil", "Refsnes") 

# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil") 

# Arbitrary Arguments
# def my_fun(*kids):
#   print("The youngest child is " + kids[1])

# my_fun("Emil", "Tobias", "Linus")

# Keyword Arguments
# def my_fun(ch3,ch2,ch1):
#   print("The yougest child is " + ch2)

# my_fun(ch1="Emly", ch2="John", ch3="Linus")

# Arbitrary Keyword Arguments
# def my_fun(**kid):
#   print("His last name is " + kid["lname"])

# my_fun(fname = "Tobias", lname = "John") 

#Default Parameter Value
# def my_fun(country= "Norway"):
#   print("I am from " + country)


# my_fun("Sweden")
# my_fun()

def my_fun(x=20):
  g="Here Tester"
  return x*2

if __name__=="__main__":
  import inspect
  print (inspect.getsource(my_fun))


#List Argument
# def my_function(food):
#   for x in food:
#     print(x)
# fruits = ["apple","orange","banana"]
# my_function(fruits)

# #Return Values
# def my_fun(x):
#   return 5*x
# print (my_fun(3))
# pass

# #Recursion Exmaple
# def tri_recursion(k):
#   if(k>0):
#     result = k+tri_recursion(k-1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)

