#Creating Class
# class MyClass:
#     x=5

# p1=MyClass()
# print(p1.x)

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# #     def myfun(self):
# #         print("Hello my name is " + self.name)

# # p1 = Person("TES",25)
# # p1.myfun()
# #print(p1.name,p1.age)
# #print(p1.age)

# class Person:
#     def __init__(mysillyobject, name, age):
#         mysillyobject.name = name
#         mysillyobject.age = age

#     def myfun(abc):
#         print ("Hello my name is " + abc.name)
#         print ("Hello my age is " + str(abc.age))

# p1 = Person("TES",25)
# p1.myfun();
#p1.age=30
#del p1.age
#p1.myfun()
#print(p1.age)

# class MyClass:
#     def myfun(self,a):
#         return a*2
# if __name__=="__main__":
#     myclass = MyClass()
#     print (myclass.myfun(a=5))

class MyClass:
     def __init__(self):
         print("Hello from init")
     def myfun(self):
         print("Hello from myfun")
if __name__=="__main__":
     myclass = MyClass()
     myclass.myfun()


