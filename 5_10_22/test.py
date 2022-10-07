class MyClass:

	def __init__(self, item):
		self.item = item
	def __len__(self):
		return len(self.item)

obj = MyClass("Hello World")
print(obj.__len__())