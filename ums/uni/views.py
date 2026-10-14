from django.shortcuts import render
from rest_framework import viewsets
from .models import Result, Enrollment, Course
from .serializers import RestultSerilizer, CourseSerializer

class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = RestultSerilizer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer




