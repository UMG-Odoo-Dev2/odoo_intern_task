mark = input("Enter Your Mark: ")
mark = int(mark)

if mark >= 0 and mark <= 100:
    if mark >= 80:
        print("Passed With Distinction")
    elif mark >= 40:
        print("Passed")
    else:
        print("Failed")
else:
    print("Wrong Input! Try Again.")