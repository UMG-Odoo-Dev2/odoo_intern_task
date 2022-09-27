ages = [30, 19, 17, 15, 21, 60, 14]
adults = list(filter(lambda age: age > 18, ages))
print(adults,"\n")

animals = ['bird', 'dog', 'snake', 'fish']
uppered_animals = list(map(lambda animal: animal.upper(), animals))
print(uppered_animals,"\n")

from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
mul= reduce((lambda x, y:x*y),li)
print(sum,"\n")
print(mul,"\n")