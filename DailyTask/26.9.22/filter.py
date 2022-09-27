from cgi import print_environ


a = "hello"
print(id(a))
b = a + "world"
print(id(b))
c = b.replace("h", "x")
print(id(c))