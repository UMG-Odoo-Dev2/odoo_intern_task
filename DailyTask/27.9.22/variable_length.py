# def show_member(*names):
#     print("type is:", type(names))#<class 'tuple'>
#     for name in names:
#         print(name)

# show_member("Kyaw Kyaw", "Aung Aung", "Aye Aye", "Su Su")

from unicodedata import name


def signup_member(**keywargs):
    print("type is:", type(keywargs))#<class 'dict'>
    for key in keywargs:
        print(keywargs[key])

signup_member(name = "Zaw Thu Htet", age = 27, gender = "Male")
