from django.urls import path
from CSVFILE import views
urlpatterns=[
    path('employee/',views.EmployeeDetails),
]