from django.db import models

# Create your models here.
class Register(models.Model):
	Gender_choise=(('m', 'Male'),('f', 'Female'))
	desg=(('student','Student'),('employee','Employee'))
	courses=(('c','C'),('c++','C++'),('python','Python Programming'),('c#','C#'),('java','Java'),('web','Web Technologies'),('php',"PHP"))
	name=models.CharField(max_length=200)
	gender=models.CharField(max_length=1,choices=Gender_choise)
	designation=models.CharField(max_length=100,choices=desg)
	college=models.CharField(max_length=500)
	course=models.CharField(max_length=100,choices=courses)	
	mobile=models.CharField(max_length=20)
	email=models.CharField(max_length=200)
	joined_date=models.DateField()
	
	def __str__(self):		
		d=str(self.joined_date)
		return self.name+" | "+self.course+" | "+d

class employee(models.Model):
	name=models.CharField(max_length=100)
	start_date=models.CharField(max_length=100)
	end_date=models.CharField(max_length=100)
	notes=models.CharField(max_length=200)

	def __str__(self):
		return self.name
