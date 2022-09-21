def show_member(**kwargs):
    print("type is",type(kwargs))
    for key in kwargs:
        print(kwargs[key])
show_member(name="Kyaw Kyaw",age=23,gender="Male")