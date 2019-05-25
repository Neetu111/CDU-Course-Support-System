from django.db import models

year_choice = [(i,i) for i in range(1, 5)]
semester_choice = [(i,i) for i in range(1,3)]
class Unit(models.Model):
	UnitCode = models.CharField(max_length=6, primary_key=True)
	UnitName = models.CharField(max_length=400)
	Type = models.CharField(max_length=2)
	Points = models.IntegerField(default=10)
	PreRequisite = models.BooleanField(default=False)

	def __str__(self):
		return self.UnitCode + ' ' + self.UnitName

class Course(models.Model):
	CourseCode = models.CharField(max_length=10, primary_key=True)
	CourseName = models.CharField(max_length=400)
	CourseType = models.CharField(max_length=100)

	def __str__(self):
		return self.CourseCode + ' ' + self.CourseName

class CourseMajor(models.Model):
	CourseCode = models.CharField(max_length=10)
	Field = models.CharField(max_length=400)
	Semester = models.IntegerField(choices=semester_choice)
	Year = models.IntegerField(choices=year_choice)
	class Meta:
		unique_together = (('CourseCode','Field'),)
	
	def __str__(self):
		return self.CourseCode + ' ' + self.Field

class PreRequisite(models.Model):
	UnitCode = models.CharField(max_length=6)
	PreRequisiteCode = models.CharField(max_length=6)
	class Meta:
		unique_together = (('UnitCode','PreRequisiteCode'),)

	def __str__(self):
		return self.UnitCode + ' ' + self.PreRequisiteCode

class SemesterUnit(models.Model):
	UnitCode = models.CharField(max_length=6)
	CourseCode = models.CharField(max_length=10)
	Field = models.CharField(max_length=400, default="Chemical Engineering")
	Semester = models.IntegerField(choices=semester_choice, default=1)
	Year = models.IntegerField(choices=year_choice, default=1)
	class Meta:
		unique_together = (('UnitCode','CourseCode','Semester','Year','Field'),)

	def __str__(self):
		return self.UnitCode + ' ' + self.CourseCode + ' ' + self.Field + ' ' + str(self.Semester) + ' ' + str(self.Year)
