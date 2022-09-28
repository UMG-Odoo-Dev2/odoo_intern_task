# sys.argv
## sys => System Specific Parameters and Functions
> Command Line Argument
- 1st element of array[sys.argv()] => its name
- sys.argv() is array for command line argument in Python
- Import sys module to use sys.argv
  - import sys
- sys.argv က Python array နဲ့ဆင်တူပီး အလုပ်လုပ်ပုံပါ ဆင်တူ
- len(), str() functions can be used with sys.argv
  - len()
    - used to count no. of args passed to cmd
    - Iteration start with 0, so it counts the name of the program as one argument
  - str()
    - used to present array as a string array
    - make displaying cmd array easier and better

> Example Program
```
import sys
print("This is the name of the program: ", sys.argv[0])
print("Argument List: ", str(sys.argv))
```
> Output (Pass cmd args)
```
(venv) D:\Project\dailyTest\odoo_intern_task\27sepJson>python argvTest.py 1 2 3
This is the name of the program:  argvTest.py
Argument List:  ['argvTest.py', '1', '2', '3']
```


