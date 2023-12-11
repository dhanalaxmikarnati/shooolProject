from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .serializers import StudentSerializer


# # Create your views here.
# # read    
# @api_view(['GET'])
# def student(request):
#     student_obj = Student.objects.all()
#     serializer = StudentSerializer(student_obj,many=True)  
#     return Response(serializer.data)
# #create
# @api_view(['POST'])
# def create_student_data(request):
#     student_obj = Student.objects.all()
#     serializer = StudentSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# #update
# @api_view(['POST'])
# def update_student_data(request,id):
#     student_obj = Student.objects.get(id=id)
#     serializer = StudentSerializer(instance=student_obj,data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# #delete
# @api_view(['DELETE'])
# def delete_user_data(request,id):
#     student_obj = Student.objects.get(id=id)
#     student_obj.delete() 
#     return Response("user is deleted") 


def students(request):
    return 'viwes'




# Read (GET all students)
@api_view(['GET'])
def get_all_students(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

# Create (POST a new student)
@api_view(['POST'])
def create_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response({"serializer.data":serializer.data,
                         "message":"successfully registered",
                         "status":"success" })  
    else:
          return Response({"status":"error",
                             "code": "INVALID-REQUEST",
                             "message": "internal server 400 issue"
                            })                      
    # return Response(serializer.errors, status=400)

# Update (PUT an existing student)
@api_view(['PUT'])
def update_student(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
         return Response({"status":"error",
                             "code": "INVALID-REQUEST",
                             "message": "internal server 400 issue"
                            }) 

    serializer = StudentSerializer(student, data=request.data,  partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response({"serializer.data":serializer.data,
                         "message":"successfully got user details",
                         "status":"success" })  
    
    return Response(serializer.errors, status=400)

# Delete (DELETE an existing student)
@api_view(['DELETE'])
def delete_student(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response({"status":"error",
                             "code": "INVALID-REQUEST",
                             "message": "internal server 400 issue"
                            }) 

    student.delete()
    return Response("Student deleted successfully", status=204)