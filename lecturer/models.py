from django.db import models

# Create your models here.
class Lecturer(models.Model):
    LecturerID = models.CharField(max_length=10)
    Name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

