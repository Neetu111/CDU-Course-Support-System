from django.db import models

# Create your models here.
class Lecturer(models.Model):
    LecturerID = models.CharField(max_length=10, primary_key = True)
    Name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def publish(self):
        self.save()

    def __str__(self):
        return self.LecturerID + ' ' + self.Name 