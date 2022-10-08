def hello_decorator(func):
	def inner1(*args, **kwargs): # step 2
		
		print("before Execution") # step 5
		
		# getting the returned value
		returned_value = func(*args, **kwargs) # step 6
		print("after Execution")
		
		# returning the value to the original frame
		return returned_value
		
	return inner1 # step 3, 

print("Starting Print")
# adding decorator to the function
@hello_decorator # step 1
def sum_two_numbers(a, b):
	print("Inside the function") # step 7
	return a + b
#sum_two_numbers = hello_decorator(sum_two_numbers)

a, b = 1, 2
# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b), '\n\n') # sum_two_numbers(a,b) is step 4, 


# Decorator with Parameter
def decorate_fun(*args, **kwargs):
	print("Inside Decorator")
	def inner(func):
		print("Inside Inner Function")
		print("I Like ", kwargs['like'])

		func()
	return inner

@decorate_fun(like = "FOODS")
def func_to():
	print("Inside actual function \n\n")
#decorate_fun(func_to)() # another way of using decorator

# anothre example of decorator with parameters
def decorate_func(x, y):
	print("Decorate Function")
	print(x,y)
	def Inner(pick):
		print("Inner")

		def wrapper(*args, **kwargs):
			print(type(pick))
			print("Inside Execution Function")
			print("Sum of value - {}".format(x+y))

			pick(*args, **kwargs)
			print(type(pick), '\n\n')
		return wrapper

	return Inner
@decorate_func(13,25)
def fun_arg(*args):
	for you in args:
		print(you)

fun_arg('You','Broke','Me','First')
	
#decorate_func(13, 25)(fun_arg)('You','Broke','Me','First')

