from django.db import models

# Create your models here.
class Unit(models.Model):
    UnitCode = models.CharField(max_length=6, primary_key=True)
    UnitName = models.CharField(max_length=400)
    Type = models.CharField(max_length=2)
    PreRequisite = models.BinaryField()
    Semester = models.DecimalField(max_digits=1, decimal_places=0)

class Course(models.Model):
    CourseCode = models.CharField(max_length=10, primary_key=True)
    CourseName = models.CharField(max_length=400)
    CourseType = models.CharField(max_length=100)

class CourseMajor(models.Model):
    CourseCode = models.CharField(max_length=10)
    Field = models.CharField(max_length=400)
    class Meta:
        unique_together = (('CourseCode','Field'),)

class PreRequisite(models.Model):
    UnitCode = models.CharField(max_length=6)
    PreRequisiteCode = models.CharField(max_length=6)
    class Meta:
        unique_together = (('UnitCode','PreRequisiteCode'),)

class SemesterUnit(models.Model):
    UnitCode = models.CharField(max_length=6)
    CourseCode = models.CharField(max_length=10)
    class Meta:
        unique_together = (('UnitCode','CourseCode'),)
