# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.template import Context, Template
from django.shortcuts import render, redirect
from django.core.context_processors import csrf
from .forms import *
from .models import Unit, Course, CourseMajor, SemesterUnit, PreRequisite
import requests

def index(request):
	form = CourseForm()
	if request.method=="POST":
		form = CourseForm(request.POST)
		course_code = request.POST.get('CourseCode')
		field = request.POST.get('Field')
		semster = request.POST.get('Semester')
		course_majors = CourseMajor.objects.all()
		model_course_code =[]
		model_field =[]
		for course_major in course_majors:
			model_course_code.append(course_major.CourseCode)
			model_field.append(course_major.Field)
		Unit_Name = SemesterUnit.objects.filter(CourseCode = course_code) 
		if course_code in model_course_code and field in model_field:		# validating the details 
			units = Unit.objects.all()
			courses = Course.objects.filter(CourseCode = course_code)
			# course_majors = CourseMajor.objects.filter(CourseCode = course_code)
			semester_unit = SemesterUnit.objects.filter(CourseCode = course_code)
			pre_requisite = PreRequisite.objects.all()
			context = {'units': units, 'courses': courses, 'course_majors':course_majors, 'semester_unit':semester_unit,'pre_requisite': pre_requisite}
			return render(request,'student/StudyPlan.html',context)
		else:
			#form = CourseForm()
			return HttpResponse(form.errors.as_data())		# just for checking 
	return render(request, 'student/index.html',{'form': form})

def StudyPlan(request):
	unitss = Unit.objects.all()
	context = {'Units': unitss}
	return render(request, 'student/StudyPlan.html', context)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
# def get_unit_code(course_code):
	# unit_code = []
	# unit_name = []
	# Semester_Unit = SemesterUnit.objects.filter(Q(CourseCode = "course_code") | Q(Semester = "semester")) # have relevant info u can use in html and get the relevant value 
	# #unit_code = SemesterUnit.UnitCode
	# #unit = Unit.objects.all()
	# #course_data = Context({'semester_unit': Semester_Unit})
	# #unit_data = Context({'unit': unit})
	# #for course_entry in course_data:
	# #	if course_entry.CourseCode == course_code:
	# #		unit_code.append(course_entry.UnitCode)
	# return Semester_Unit

# def get_unit_name(unit_code):
	# unit_name = []
	# unit = Unit.objects.all()
	# unit_data = Context({'unit': unit})
	# for unit_entry in unit_data:
		# if unit_entry.UnitCode in unit_code:
			# unit_name.append(unit_entry.UnitName)
	# return unit_name
	
# def get_pre_req(unit_code):
	# pre_req_Unit = PreRequisite.objects.filter(Q(CourseCode = "course_code") | Q(Semester = "semester"))
	# # pre_req = {}
	# # unit_code = []
	# # unit_name = []
	# # course_data = context({'semester_unit': SemesterUnit})
	# # unit_data = context({'unit': Unit})
	# # for course_entry in course_data:
		# # if course_entry.CourseCode == course_code:
			# # unit_code.append(course_entry.UnitCode)
	# # for unit_entry in unit_data:
		# # if unit_entry.UnitCode in unit_code:
			# # unit_name.append(unit_entry.UnitName)
	# # return unit_name
	
	
	
	
	