from django import forms
from .models import *

class CourseForm(forms.ModelForm):
    class Meta:
        model = CourseMajor
        fields = ('CourseCode', 'Field', 'Semester')