class Employee:
	__id=10

	def get_id(self):
		print("Id inside class",self.__id)

emp=Employee()
emp.get_id()
print("Id outside class",emp.__id)