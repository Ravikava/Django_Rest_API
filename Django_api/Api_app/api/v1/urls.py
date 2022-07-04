from django.urls import path
from .views import *

urlpatterns = [
    path('empapi/',EmployeeApi.as_view()),
    path('empapi/<int:pk>/',EmployeeApi.as_view()),
]
