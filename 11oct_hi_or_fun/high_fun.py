def loud(text):
    return text.upper()

def whisper(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(loud)
hello(whisper)

# Function as a parameter

def sum_num(nums): # normal function
    return sum(nums)

def higher_order_func(func, lst): # function as a parameter
    summing = func(lst)
    return summing

result = higher_order_func(sum_num, [2,4,6,8])
print(result)

# Functoin as return value

def square(x): # a square function
    return x**2
def cube(x): # a cube function
    return x**3
def absolute(x): # a absolute function
    if x>=0:
        return x
    else:
        return -(x)

def high_ord_func(type): # returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = high_ord_func('square')
print(result(7))
result = high_ord_func('cube')
print(result(7))
result = high_ord_func('absolute')
print(result(-7))

# Nani Nani
nums = [1,3,5,7,9]

def square(n):
    return n**2
sq_nums = map(square,nums)
#sq_nums = map(lambda n : n**2, nums)
print(list(sq_nums), type(sq_nums))


fruits = ['Avocado','WaterMelon','Papaya','Guava']

def fruitUp(fruit):
    return fruit.upper()
result = list(map(fruitUp,fruits))
#result = list(map(lambda fruit : fruit.upper(), fruits))
print(result, type(result))

# Filter Function

nums = [214, 333, 487, 967, 666, 555, 478]

def is_even(enum):
    if enum % 2 == 0:
        return True
    else:
        return False

even_num = list(filter(is_even, nums))

#even_num = list(filter(lambda num : num%2 == 0, nums))
print(even_num, type(even_num))

# Reduce function
import functools

letters = ['C','H','A','O','S']

def redFun(x, y):
    return x+y
word = functools.reduce(redFun, letters)

#word = functools.reduce(lambda x, y : x + y, letters)
print(word)

listNum = ['5','24','6','8','10']
redNum = functools.reduce(lambda x, y: x + y, listNum)
print(redNum)

nunum = [5,8,7,9,3,6,7]

result = functools.reduce(lambda x, y: x - y, nunum)
print(result, type(result))