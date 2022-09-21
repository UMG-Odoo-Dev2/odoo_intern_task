try:
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    c=a/b
    print(c)
except Exception:
    print("Can't divide by zero,Please use b as greater than zero!")