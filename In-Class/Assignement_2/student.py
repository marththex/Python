#student.py
#Create a Student Class

class Student(object):
	def __init__(self, firstName = "", lastName = "", age = 0, GPA = 0.0):
		self.firstName = firstName
		self.LastName = lastName
		self.age = age
		self.GPA = GPA
	
		
	def updateGPA(self,newGPA):
		GPA = newGPA
		
	def __str__(self):
		return ("Hello, my name is blah" )
		
student1 = Student("Marcus","Chong", 20 ,3.8)
print(student1.firstName)


		
	
	
	