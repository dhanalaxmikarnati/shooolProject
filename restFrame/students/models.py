from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Student(models.Model):
    studentName=models.CharField(max_length=50)
    studentEmail=models.EmailField()
    roll_number=models.IntegerField()
    # phone_number= PhoneNumberField(null=False, blank=False, unique=True)
    
    
    def __str__(self):
	    return self.studentName
