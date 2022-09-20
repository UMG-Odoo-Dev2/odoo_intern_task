class Employee:
	__id=10
	def change_id(self,id):
		if(id>20):
			print("Id greater than 20 is not permitted !")
		else:
			self.__id=id
			print("Id inside class affter change",self.__id)
	def get_id(self):
		print("Id inside class",self.__id)

emp=Employee()
emp.get_id()
emp.change_id(5)
emp.change_id(50)

