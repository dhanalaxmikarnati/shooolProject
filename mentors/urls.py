from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import  settings

urlpatterns = [
    
    
    path('logout',views.logout,name='logout'),
    path('',views.school,name="school"),
   
    path('teachers',views.teachers,name="teachers"),
    path('courses',views.courses,name="courses"),
    path('grades',views.grades,name="grades"),
    path('loging',views.loging,name='loging'),
    path('registers',views.registers,name='registers'),
    # path('students/',views.student,name="student"),
    path('add_student/',views.add_student,name="add_student"),
    path('success',views.success,name="success"),
    path('mentors',views.mentors,name="mentors"),
    
    
]
urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




