from django.contrib import admin
from .models import Unit, Course, PreRequisite, SemesterUnit, CourseMajor

admin.site.register(Unit)
admin.site.register(Course)
admin.site.register(PreRequisite)
admin.site.register(SemesterUnit)
admin.site.register(CourseMajor)