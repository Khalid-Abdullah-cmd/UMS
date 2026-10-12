from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class User(AbstractUser):

    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        PROFESSOR = "PROFESSOR", "Professor"
        STUDENT = "STUDENT", "Student"

    email = models.EmailField("email address", unique=True)
    role = models.CharField(
        max_length=20, choices=Role.choices, default=Role.STUDENT
    )
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.get_full_name() or self.username} ({self.role})"


class Course(models.Model):

    
    title = models.CharField(max_length=200)
    capacity = models.PositiveIntegerField()
    professor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="courses_taught",
        limit_choices_to={"role": User.Role.PROFESSOR},
    )

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="enrollments",
        limit_choices_to={"role": User.Role.STUDENT},
    )
    course = models.ForeignKey(
        Course, on_delete=models.PROTECT, related_name="enrollments"
    )
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["student", "course"], name="unique_student_course"
            )
        ]

    def __str__(self):
        return f"{self.student} -> {self.course}"


class Result(models.Model):


    enrollment = models.OneToOneField(
        Enrollment, on_delete=models.PROTECT, related_name="result"
    )
    grade = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    graded_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.enrollment}: {self.grade}"