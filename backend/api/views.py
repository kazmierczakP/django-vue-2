from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class StudentApi(APIView):
    def get(self, request):
        students = []
        return Response({'msg': students})