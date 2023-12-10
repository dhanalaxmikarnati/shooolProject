from django.shortcuts import redirect, render
from django.contrib import messages
from mentors.models import Mentor
from students.models import Student
from .forms import AddStudentForm  # Create a form to add students to mentor

# Create your views here.

def school(request):
    return render(request, 'school.html')
def add_student(request):
    students= Student.objects.all()
    mentors = Mentor.objects.all()
    context = {'students': students, 
                'mentors': mentors }
    if request.method == 'POST':
        mentor_email = request.POST.get('mentor_email')
        mentor = Mentor.objects.get(email=mentor_email)

        # Extract student details from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        unique_code = request.POST.get('unique_code')
        aadhar = request.POST.get('aadhar')
        class_level = request.POST.get('class_level')
        address = request.POST.get('address')
        section = request.POST.get('section')
        pics = request.FILES.get('pics') #if 'pics' in request.FILES else None

        # Create a new student instance associated with the mentor
        student = Student.objects.create(
            mentor=mentor,
            name=name,
            email=email,
            unique_code=unique_code,
            aadhar=aadhar,
            class_level=class_level,
            address=address,
            section=section,
            pics=pics
        )
        messages.info(request,"student is added")
        student.save()
        return render(request, 'add_student.html', context)  
    return render(request, 'add_student.html', context)
    
def mentors(request):
    return 'views'

# def student(request):
    
#     students= Student.objects.all()
#     context = {'students': students }
#     return render(request, 'students.html', context)
    
    
def teachers(request):
    return render(request,'teachers.html')
def courses(request):
    return render(request,'courses.html')
def grades(request):
    return render(request,'grades.html')
def loging(request):
    return render(request,'loging.html')
def registers(request):
    return render(request,'registers.html')
def success(request):
   return render(request, 'success.html' )
   
def logout(request):
    return redirect('/')         