from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import  settings


urlpatterns = [
    path('students/',views.students),
    path('get/',views.get_all_students),
    path('add/',views.create_student),
    path('update/<int:id>',views.update_student),
    path('delete/<int:id>',views.delete_student)
    # path('student/',views.student),
    # path('add/',views.create_student_data),
    # path('update/<int:id>',views.update_student_data),
    # path('delete/<int:id>',views.delete_user_data)
]
urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
