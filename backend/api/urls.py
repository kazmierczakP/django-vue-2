from django.urls import path
from . import views

urlpatterns=[
    path('students', views.StudentApi.as_view()),
] 