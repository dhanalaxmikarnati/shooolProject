from django.urls import path
from . import views


urlpatterns = [
    # path('',views.login),
    # path('registers/',views.register),
    path('mentor/<int:mentor_id>/students/', views.mentor_students, name='mentor_students'),
    path('add_student',views.add_student),
    
    path('logout',views.logout,name='logout'),
    path('',views.school,name="school"),
    path('students',views.students,name="students"),
    path('teachers',views.teachers,name="teachers"),
    path('courses',views.courses,name="courses"),
    path('grades',views.grades,name="grades"),
    path('loging',views.loging,name='loging'),
    path('registers',views.registers,name='registers'),
    
    
]



