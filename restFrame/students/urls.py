from django.urls import path
from . import views


urlpatterns = [
    path('student/',views.student),
    path('add/',views.create_student_data),
    path('update/<int:id>',views.update_student_data),
    path('delete/<int:id>',views.delete_user_data)
]