from django.db import models
from students.models import Student 

# Create your models here.
class Mentor(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email=models.EmailField()
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=12)
    
    students = models.ManyToManyField(Student) # Many-to-Many relationship

    def __str__(self):
	    return self.username
 



    

