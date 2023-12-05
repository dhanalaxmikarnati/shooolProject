from django.shortcuts import redirect, render
from django.shortcuts import render, get_object_or_404
from .models import Mentor,Student
from .forms import AddStudentForm  # Create a form to add students to mentor

def add_student_to_mentor(request, mentor_id):
    mentor = get_object_or_404(Mentor, pk=mentor_id)
    if request.method == 'POST':
        form = AddStudentForm(request.POST)
        if form.is_valid():
            student_email = form.cleaned_data['student_email']
            student = Student.objects.get(studentEmail=student_email)  # Get student by email
            mentor.students.add(student)  # Add student to mentor's students
            # You might want to add more logic or redirect to a success page here
    else:
        form = AddStudentForm()
    
    return render(request, 'add_student.html', {'form': form})


def mentor_students(request, mentor_id):
    mentor = Mentor.objects.get(pk=mentor_id)
    students = mentor.students.all()  # Access all students associated with this mentor
    return render(request, 'mentor_students.html', {'students': students})


def add_student(request):
    return render(request,'add_student.html')
def school(request):
    return render(request,'school.html')
def students(request):
    return render(request,'students.html')
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

def logout(request):
    return redirect('/')         