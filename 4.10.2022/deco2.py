def hello_decorator(func):
    def inner1(*args,**kwargs):
         
        print("before Execution")
        # print(kwargs['a'])
         
        # getting the returned value
        func(*args)
        print("after Execution")
         
        # returning the value to the original frame
        
         
    return inner1
@hello_decorator
def sum_two_numbers(num):
    print(num)
    print(type(num))
    # return dict
 
# a, b = 1, 2
dict={"a":"father","b":"mother"}
sum_two_numbers(dict)