from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from .models import Students
from .serializers import StudentSerializer


class StudentsApi(APIView):
    def get(self, request):
        # alternate to serializer u can:
        # - use model_to_dict
        # - make list(Student.objects.values())
        students = Students.objects.all()
        students_serializer = StudentSerializer(students, many=True)
        return Response(students_serializer.data)
    def post(self, request):
        students_data = JSONParser().parse(request)
        print(students_data)
        students_serializer = StudentSerializer(data=students_data)
        try:
            students_serializer.is_valid()
            students_serializer.save()
            return Response({"msg": "Added Successfully"})
        except Exception as e:
            return Response({"msg": f"{e}"})

'''
class StudentsViewSet(ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
'''

class StudentApi(APIView):
    def get(self, request, pk):
        student = Students.objects.get(StudId=pk)
        student_serializer = StudentSerializer(student)
        return Response(student_serializer.data)
    def put(self, request, pk):
        student_data = JSONParser().parse(request)
        student = Students.objects.get(StudId=pk)
        student_serializer = StudentSerializer(student, data=student_data)
        try:
            student_serializer.is_valid()
            student_serializer.save()
            return Response({"msg": "Updated Successfully"})
        except Exception as e:
            return Response({"msg": f"{e}"})
    def delete(self, request, pk):
        student = Students.objects.get(StudId=pk)
        try:
            student.delete()
            return Response({"msg": "Deleted Successfully"})
        except Exception as e:
            return Response({"msg": f"{e}"})
