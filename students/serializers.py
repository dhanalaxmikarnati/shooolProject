from students.models import Student
from mentors.models import Mentor
from rest_framework import serializers
# from django.contrib.auth.models import User
from rest_framework import serializers,validators
from .models import  *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        extra_kwargs = {
            "mentor": {"write_only": True},
            "email": {
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        Student.objects.all(), f"A student with that Email already exists.",
                        # Mentor.objects.all(), f"mentor assigned already."
                    )
                ],
            },
        }

    def create(self, validated_data):
        user = Student.objects.create_user(
            mentor=validated_data["mentor"],
            email=validated_data["email"],
            unique_code=validated_data["password"],
            name=validated_data["name"],
            aadhar=validated_data["aadhar"],
            pics=validated_data["pics"],
            class_level=validated_data["class_level"],
            address=validated_data["address"],
            section=validated_data["section"],
            
        )
        return user
    def create(self, validated_data):
        # Pop 'pics' from validated_data to handle separately
        pics= validated_data.pop('pics', None)
        
        # Create the student without the 'pics' field
        student = Student.objects.create(**validated_data)
        
        # Add 'pics' separately if a file was provided
        if pics:
            student.pics = pics
            student.save()

        return student
