from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('add_attendance/', views.add_attendance, name='add_attendance'),
    path('students/', views.student_list, name='student_list'),
    path('add_student/', views.add_student, name='add_student'),
    path('subjects/', views.subject_list, name='subject_list'),
    path('add_subject/', views.add_subject, name='add_subject'),

    # Admin Panel URL
    path('admin/', admin.site.urls),  
]
