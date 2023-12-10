from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .serializers import StudentSerializer


# Create your views here.
# read    
@api_view(['GET'])
def student(request):
    student_obj = Student.objects.all()
    serializer = StudentSerializer(student_obj,many=True)  
    return Response(serializer.data)
#create
@api_view(['POST'])
def create_student_data(request):
    student_obj = Student.objects.all()
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#update
@api_view(['POST'])
def update_student_data(request,id):
    student_obj = Student.objects.get(id=id)
    serializer = StudentSerializer(instance=student_obj,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#delete
@api_view(['DELETE'])
def delete_user_data(request,id):
    student_obj = Student.objects.get(id=id)
    student_obj.delete() 
    return Response("user is deleted") 


def students(request):
    return 'viwes'