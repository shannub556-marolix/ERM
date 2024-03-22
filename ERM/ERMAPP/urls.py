from django.contrib import admin
from django.urls import path
from.import views


urlpatterns = [

    path('employee',views.Employee_data),
    path('attendance', views.Attendance_data),
    path('list',views.Attendance_list),
]
