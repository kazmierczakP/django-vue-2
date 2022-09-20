from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Students
from .serializers import StudentSerializer

class StudentApi(APIView):
    def get(self, request):
        # alternate to serializer u can:
        # - use model_to_dict
        # - make list(Student.objects.values())
        students = Students.objects.all()
        students_serializer = StudentSerializer(students, many=True)
        return Response(students_serializer.data)