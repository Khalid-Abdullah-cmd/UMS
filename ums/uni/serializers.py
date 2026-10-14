from rest_framework import serializers
from .models import Result, Course


class RestultSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ['enrollment','grade']



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['title', 'capacity', 'professor']