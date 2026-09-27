from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ...


class Course(models.Model):
    title = models.CharField(max_length=200)
    capacity = models.PositiveIntegerField

class Enrollment(models.Model):
    ...

class Result(models.Model):
    ...             
