from django import forms
from .models import *


def unique(list):
    # intilize a null list
    unique_list = []
    # traverse for all elements
    for x in list:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)

class CourseForm(forms.ModelForm):
    course_codes = [str(course_code['CourseCode']) for course_code in CourseMajor.objects.all().values('CourseCode').distinct()]
    CourseCode = forms.ChoiceField(choices=([(course_code, course_code) for course_code in course_codes]))
    fields = [str(field['Field']) for field in CourseMajor.objects.all().values('Field').distinct()]
    Field = forms.ChoiceField(choices=([(field, field) for field in fields]))
    class Meta:
        model = CourseMajor
        fields = ('CourseCode', 'Field', 'Semester', 'Year')









