# from django.contrib.auth.models import Student
from rest_framework import serializers
from .models import  *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        

    # def create(self, validated_data):
    #     student = Student.objects.create_user(
    #         firstname=validated_data["firstname"],
    #         username=validated_data["username"],
    #         email=validated_data["email"],
    #         password=validated_data["password"],
            
    #     )
    #     return user

