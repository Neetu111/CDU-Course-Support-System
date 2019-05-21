from django.core.serializers import json
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import *
from .models import Unit, Course, CourseMajor, SemesterUnit, PreRequisite


def index(request):
	form = CourseForm()
	if request.method=="POST":
		form = CourseForm(request.POST)
		course_code = request.POST.get('CourseCode')
		field = request.POST.get('Field')
		semester = request.POST.get('Semester')
		course_majors = CourseMajor.objects.all()
		model_course_code =[]
		model_field =[]
		for course_major in course_majors:
			model_course_code.append(course_major.CourseCode)
			model_field.append(course_major.Field)
		if course_code in model_course_code and field in model_field:
			return HttpResponseRedirect(reverse('student:study_plan', args=[field, course_code]))   #redirect(reverse('study_plan'), course_field=field)
		else:
			form = CourseForm()
	return render(request, 'student/index.html',{'form': form})

def study_plan(request, course_field, course_code):
	course_id = CourseMajor.objects.filter(Q(Field = course_field) | Q(CourseCode=course_code))
	unit_id = SemesterUnit.objects.filter(CourseCode=course_code)
	unit_codes = SemesterUnit.objects.filter(CourseCode=course_code).values('UnitCode')
	desired_units = Unit.objects.filter(UnitCode__in = unit_codes)
	pre_requisite_units = PreRequisite.objects.filter(UnitCode__in=unit_codes)
	pre_requisite_unit = [{'UnitCode': pre_requisite.UnitCode, 'PreRequisiteCode': pre_requisite.PreRequisiteCode} for pre_requisite in pre_requisite_units]
	context = {'pre_requisite_units': pre_requisite_unit, 'units': desired_units, 'course_field':course_field, 'course_code':course_code}
	return render(request, 'student/study_plan.html', context)

unit_for_div = []
def check_prerequisite(request, course_field, course_code):
	course_id = CourseMajor.objects.filter(Q(Field=course_field) | Q(CourseCode=course_code))
	unit_id = SemesterUnit.objects.filter(CourseCode=course_code)
	unit_codes = SemesterUnit.objects.filter(CourseCode=course_code).values('UnitCode')
	desired_units = Unit.objects.filter(UnitCode__in=unit_codes)
	pre_requisite_units = PreRequisite.objects.filter(UnitCode__in=unit_codes)
	pre_requisite_unit = [{'UnitCode': pre_requisite.UnitCode, 'PreRequisiteCode': pre_requisite.PreRequisiteCode} for pre_requisite in pre_requisite_units]
	try:
		selected_unit = Unit.objects.get(UnitCode = request.POST['unit'])
		if selected_unit not in unit_for_div:
			unit_for_div.append(selected_unit)
		print("trial                value")
		print(unit_for_div)
	except (KeyError, Unit.DoesNotExist):
		context = {'pre_requisite_units':pre_requisite_unit, 'units': desired_units, 'course_field': course_field, 'course_code': course_code, 'error_message':"not working"}
		return render(request, 'student/study_plan.html', context)
	else:
		if selected_unit.PreRequisite:
			context = {'pre_requisite_units':pre_requisite_unit, 'units': desired_units, 'course_field': course_field, 'course_code': course_code, 'unit_for_div': unit_for_div}
			return render(request, 'student/study_plan.html', context)
		else:
			context = {'pre_requisite_units':pre_requisite_unit, 'units': desired_units, 'course_field': course_field, 'course_code': course_code, 'unit_for_div': unit_for_div}
			return render(request, 'student/study_plan.html', context)





def FinalStudyPlan(request, unit_code):
	unit = get_object_or_404(Unit, pk=unit_code)
	units = Unit.objects.all()
	courses = Course.objects.all()
	course_majors = CourseMajor.objects.all()
	semester_unit = SemesterUnit.objects.all()
	pre_requisite = PreRequisite.objects.all()
	try:
		selected_unit = unit.unit_get.get(pk=request.POST['unit'])
	except (KeyError, Unit.DoesNotExist):
		return render(request, 'student/study_plan.html', {'error_message':"You did not select any Unit"})




