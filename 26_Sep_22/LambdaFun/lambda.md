# Using lambda() Function with filter()
- It takes in a function and a list as arguments.
- ဒီfunctionက listထဲ မှာ itemsအားလုံးကို callခေါ်ပြီး အဲ့ဒီfunctionသည် True သို့ evaluatesလုပ်တဲ့ items များပါ၀င်သည့် new listအသစ်ကို return ပြန်ပေးတယ်။

- Example: ***Filter all people having age more than 18, using lambda and filter() function***
   ``` 
    ages = [30, 19, 17, 15, 21, 60, 14]
    adults = list(filter(lambda age: age > 18, ages))
    print(adults)
   ```
- Output:
   ```
   [30, 19, 21, 60]
   ```
# Using lambda() Function with map()
- It takes in a function and a list as an argument.
- lambda function နှင့် listတစ်ခုကနေ function ကို called ခေါ်ပြီး item တစ်ခုစီအတွက် အဲ့ဒီ functionကနေ returned ပြန်ပေးလိုက်တဲ့ lambda modified items အားလုံး ပါ၀င်သည့် new list ကို returned ပြန်ပေးပါတယ်။

- Example: ***Transform all elements of a list to upper case using lambda and map() function***
```
animals = ['bird', 'dog', 'snake', 'fish']
uppered_animals = list(map(lambda animal: animal.upper(), animals))
print(uppered_animals,"\n")
```
> <span style="color:green;font-weight:700;font-size:15px">In this example, here we intend to change all animal names
> and then do to upper case and return the same </span>
- Output:
```
['BIRD', 'DOG', 'SNAKE', 'FISH']
```

# Using lambda() Function with reduce()
- It takes in a function and a list as an argument.
- function ကို lambda functionဖြင့် ခေါ်ပြီး an iterable ထပ်ခါတလဲလဲ ပြုလုပ်နိုင်ပြီး reduced လုပ်ထားသော new result အသစ်ကို returned ပြန်ပေးသည်။ 
- ၎င်းသည် repetitive operation ထပ်ခါတလဲလဲ လုပ်ဆောင်နိုင်သော pairs of the iterable အတွဲများပေါ်တွင် လုပ်ဆောင်ပါတယ်။ 
- reduce() function သည် belongs to the  <span style="color:green;font-weight:700;font-size:15px">functools</span> module.

-Example: ***Sum of all elements in a list using lambda and reduce() function***
```
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
mul= reduce((lambda x, y:x*y),li)
print(sum,"\n")
print(mul,"\n")
```
> <span style="color:green;font-weight:700;font-size:15px">In this example, reduce() with lambda()
and then to get sum of a list </span>
- Output:
```
193 
40000000
```
