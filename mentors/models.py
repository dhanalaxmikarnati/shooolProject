from django.db import models

class Mentor(models.Model):
    mentorName= models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.email