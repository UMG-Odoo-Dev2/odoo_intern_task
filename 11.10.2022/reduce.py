import functools
numbers_str = ['1', '2', '3', '4', '5','6']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = functools.reduce(add_two_nums, numbers_str)
print(total) 