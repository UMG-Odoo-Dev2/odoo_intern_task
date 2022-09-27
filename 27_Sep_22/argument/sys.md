# sys 
> System-specific parameters and functions
- sys module သည် Python runtime environment ၏ မတူညီသော  different parts များကို manipulate လုပ်ရန် အသုံးပြုတဲ့ functionsနှင့် variable များကို provides လုပ်ပေးပါတယ်။
- Remember that sys.argv[0] is the name of the script. 
- Here – Script name is argument.py 
```
import sys

print("This is the name of the program:", sys.argv[0])
  
print("\nArgument List:", str(sys.argv))

print("\nNumber of elements including the name of the program:",len(sys.argv))
print("\nNumber of elements excluding the name of the program:",(len(sys.argv)-1))
print("\nArgument List:",str(sys.argv))
```
- In this program, the output is:
``` 
This is the name of the program: argument.py 
```
- This is ***the name of the script***
```
Number of elements including the name of the program: 4 
```
- Therefore no; of element is 4 because we write the list of command line arguments ***python argument.py 2 4 6***"  (This is len(sys.argv))
```
Number of elements excluding the name of the program: 3
```
- because of (len(sys.argv)-1) ) and then the output shows argument list as below:
```
Argument List: ['argument.py', '2', '4', '6']
```
- Another Example:
```
add = 0.0
# Getting the length of command
# line arguments
n = len(sys.argv)
  
for i in range(1, n):
    add += float(sys.argv[i])
  
print ("the sum is :", add)
```
- The output is:
```
the sum is : 7.5
```
- In this program, the Argument List: ['argument.py', '2.4', '2.5', '2.6'] (***because we write the list of command line arguments "***python argument.py 2.4 2.5 2.6 ***" )