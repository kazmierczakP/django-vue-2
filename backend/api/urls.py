from django.urls import path
from . import views

urlpatterns=[
    path('students/', views.StudentsApi.as_view()),
    path('students/<str:pk>/', views.StudentApi.as_view()),
]

'''
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('students', views.StudentsViewSet)
urlpatterns = router.urls
'''