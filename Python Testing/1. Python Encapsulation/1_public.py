    class Employee:
	id=10

	def get_id(self):
		print("Id inside class",self.id)

emp=Employee()
emp.get_id()
print("Id outside class",emp.id)