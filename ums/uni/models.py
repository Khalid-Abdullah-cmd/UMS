from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ...


class Course(models.Model):
    title = models.CharField(max_length=200)
    capacity = models.PositiveIntegerField()
    professor_id = models.ForeignKey()

class Enrollment(models.Model):
    student_id = models.ForeignKey()
    course_id = models.ForeignKey()

class Result(models.Model):

    course_id = models.ForeignKey()
    student_id = models.ForeignKey()
    grade = models.IntegerField()

    