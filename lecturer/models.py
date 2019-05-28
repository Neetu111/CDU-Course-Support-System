from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Lecturer(models.Model):
    LecturerID = models.CharField(max_length=10)
    Name = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.LecturerID