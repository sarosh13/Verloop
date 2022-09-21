from django.shortcuts import render
from .models import Manager, Student
from .serializers import ManagerSerializer,StudentSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

class ManagerListView(ListCreateAPIView): #it will automaticall handle the get and post request. also action methods.
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

class ManagerDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

class StudentListView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
