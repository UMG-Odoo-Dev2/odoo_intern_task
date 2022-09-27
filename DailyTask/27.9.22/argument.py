def Signup(username, password):
    message = username + "account is ready!"
    return message

name = input("Enter account name:")
print(Signup(name, name))