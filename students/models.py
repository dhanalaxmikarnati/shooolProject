from django.db import models
from mentors.models import Mentor

class Student(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    unique_code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    aadhar = models.CharField(max_length=12)
    pics = models.ImageField(upload_to='student_pics', null=True, blank=True)
    class_level = models.CharField(max_length=20)
    address = models.TextField()
    section = models.CharField(max_length=10)

    def __str__(self):
        return self.email