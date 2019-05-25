from django.db.models import Q
from django.forms import model_to_dict
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import *
from .models import Unit, Course, CourseMajor, SemesterUnit, PreRequisite


dict_unit_for_div = {}
unit_for_div = []
current_unit_point = []

def index(request):
	dict_unit_for_div.clear()
	del unit_for_div[:]
	del current_unit_point[:]
	error_message = ""
	form = CourseForm()
	if request.method=="POST":
		form = CourseForm(request.POST)
		course_code = request.POST.get('CourseCode')
		field = request.POST.get('Field')
		semester = request.POST.get('Semester')
		year = request.POST.get('Year')
		course_majors = CourseMajor.objects.all()
		model_course_code =[]
		model_field =[]
		for course_major in course_majors:
			model_course_code.append(course_major.CourseCode)
			model_field.append(course_major.Field)
		if course_code in model_course_code and field in model_field and int(semester) > 0 and int(semester) < 3:
			return HttpResponseRedirect(reverse('student:study_plan', args=[field, course_code, semester, year]))   #redirect(reverse('study_plan'), course_field=field)
		else:
			error_message = "Invalid values for \n"
			print(error_message)
			if course_code not in model_course_code:
				error_message += "Course Code \n"
			if field not in model_field:
				error_message += "Field \n"
			if int(semester) < 0 and int(semester) > 3:
				error_message += "Semester \n"
			form = CourseForm()
	context = {'form': form, 'error_message': error_message}
	return render(request, 'student/index.html', context)

def study_plan(request, course_field, course_code, semester, year):
	unit_for_div = []
	unit_codes = SemesterUnit.objects.filter(Q(CourseCode=course_code) & Q(Field=course_field.strip()) & Q(Semester=semester)).values('UnitCode')
	desired_units = Unit.objects.filter(UnitCode__in = unit_codes)
	pre_requisite_units = PreRequisite.objects.filter(UnitCode__in=unit_codes)
	pre_requisite_unit = [{'UnitCode': pre_requisite.UnitCode, 'PreRequisiteCode': pre_requisite.PreRequisiteCode} for pre_requisite in pre_requisite_units]
	context = {'pre_requisite_units': pre_requisite_unit, 'units': desired_units, 'course_field':course_field, 'course_code':course_code, 'semester': semester, 'year':year}
	return render(request, 'student/study_plan.html', context)

def check_prerequisite(request, course_field, course_code, semester, year):
	point_error_message = ""
	unit_codes = SemesterUnit.objects.filter(Q(CourseCode=course_code) & Q(Field=course_field.strip()) & Q(Semester=semester)).values('UnitCode')
	desired_units = Unit.objects.filter(UnitCode__in=unit_codes)
	pre_requisite_units = PreRequisite.objects.filter(UnitCode__in=unit_codes)
	pre_requisite_unit = [{'UnitCode': pre_requisite.UnitCode, 'PreRequisiteCode': pre_requisite.PreRequisiteCode} for pre_requisite in pre_requisite_units]
	try:
		selected_unit = Unit.objects.get(UnitCode = request.POST['unit'])
		dict_selected_unit = model_to_dict(selected_unit)
		if dict_selected_unit['UnitName'] not in dict_unit_for_div:
			current_unit_point.append(selected_unit.Points)
			if sum(current_unit_point) <= 40:
				dict_unit_for_div[dict_selected_unit['UnitName']]=dict_selected_unit
				unit_for_div.append(selected_unit)
			else:
				del current_unit_point[-1]
				point_error_message = "Total points for current selected unit is "+str(sum(current_unit_point)) + "this total can not exceed 40"
	except (KeyError, Unit.DoesNotExist):
		context = {'pre_requisite_units':pre_requisite_unit, 'units': desired_units, 'course_field': course_field, 'course_code': course_code, 'semester':semester, 'year':year, 'error_message':"not working"}
		return render(request, 'student/study_plan.html', context)
	else:
		if selected_unit.PreRequisite:
			context = {'pre_requisite_units':pre_requisite_unit, 'units': desired_units, 'course_field': course_field, 'course_code': course_code, 'semester':semester, 'year':year, 'unit_for_div': unit_for_div, 'dict_unit_for_div':dict_unit_for_div, 'point_error_message':point_error_message}
			return render(request, 'student/study_plan.html', context)
		else:
			context = {'pre_requisite_units':pre_requisite_unit, 'units': desired_units, 'course_field': course_field, 'course_code': course_code, 'semester':semester, 'year':year, 'unit_for_div': unit_for_div, 'dict_unit_for_div':dict_unit_for_div, 'point_error_message':point_error_message}
			return render(request, 'student/study_plan.html', context)

def delete_unit(request, course_field, course_code, semester, year):
	point_error_message = ""
	unit_codes = SemesterUnit.objects.filter(
		Q(CourseCode=course_code) & Q(Field=course_field.strip()) & Q(Semester=semester)).values('UnitCode')
	desired_units = Unit.objects.filter(UnitCode__in=unit_codes)
	pre_requisite_units = PreRequisite.objects.filter(UnitCode__in=unit_codes)
	pre_requisite_unit = [{'UnitCode': pre_requisite.UnitCode, 'PreRequisiteCode': pre_requisite.PreRequisiteCode} for
						  pre_requisite in pre_requisite_units]
	print("                reached here            ")
	try:
		selected_unit = Unit.objects.get(UnitCode=request.POST['div_unit'])
		print("                here                   ")
		print(selected_unit)
		dict_selected_unit = model_to_dict(selected_unit)
		if dict_selected_unit['UnitName'] in dict_unit_for_div:
			del dict_unit_for_div[dict_selected_unit['UnitName']]
			current_unit_point.remove(selected_unit.Points)
			unit_for_div.remove(selected_unit)
	except (KeyError, Unit.DoesNotExist):
		context = {'pre_requisite_units': pre_requisite_unit, 'units': desired_units, 'course_field': course_field,
				   'course_code': course_code, 'semester': semester, 'year': year, 'error_message': "not working"}
		return render(request, 'student/study_plan.html', context)
	else:
		if selected_unit.PreRequisite:
			context = {'pre_requisite_units': pre_requisite_unit, 'units': desired_units, 'course_field': course_field,
					   'course_code': course_code, 'semester': semester, 'year': year, 'unit_for_div': unit_for_div,
					   'dict_unit_for_div': dict_unit_for_div, 'point_error_message': point_error_message}
			return render(request, 'student/study_plan.html', context)
		else:
			context = {'pre_requisite_units': pre_requisite_unit, 'units': desired_units, 'course_field': course_field,
					   'course_code': course_code, 'semester': semester, 'year': year, 'unit_for_div': unit_for_div,
					   'dict_unit_for_div': dict_unit_for_div, 'point_error_message': point_error_message}
			return render(request, 'student/study_plan.html', context)

def common_unit(request, course_field, course_code, semester, year):
	unit_for_div = []
	unit_codes = SemesterUnit.objects.filter(
		Q(CourseCode=course_code) & Q(Field=course_field.strip()) & Q(Semester=semester)).values('UnitCode')
	desired_units = Unit.objects.filter(Q(UnitCode__in=unit_codes) & Q(Type='CU'))
	pre_requisite_units = PreRequisite.objects.filter(UnitCode__in=unit_codes)
	pre_requisite_unit = [{'UnitCode': pre_requisite.UnitCode, 'PreRequisiteCode': pre_requisite.PreRequisiteCode} for
						  pre_requisite in pre_requisite_units]
	try:
		selected_unit = Unit.objects.get(UnitCode=request.POST['unit'])
		dict_selected_unit = model_to_dict(selected_unit)
		if dict_selected_unit['UnitName'] not in dict_unit_for_div:
			current_unit_point.append(selected_unit.Points)
			if sum(current_unit_point) <= 40:
				dict_unit_for_div[dict_selected_unit['UnitName']] = dict_selected_unit
				unit_for_div.append(selected_unit)
			else:
				del current_unit_point[-1]
				point_error_message = "Total points for current selected unit is " + str(
					sum(current_unit_point)) + "this total can not exceed 40"
	except (KeyError, Unit.DoesNotExist):
		context = {'pre_requisite_units': pre_requisite_unit, 'units': desired_units, 'course_field': course_field,
				   'course_code': course_code, 'semester': semester, 'year': year, 'error_message': "not working"}
		return render(request, 'student/study_plan.html', context)
	else:
		if selected_unit.PreRequisite:
			context = {'pre_requisite_units': pre_requisite_unit, 'units': desired_units, 'course_field': course_field,
					   'course_code': course_code, 'semester': semester, 'year': year, 'unit_for_div': unit_for_div,
					   'dict_unit_for_div': dict_unit_for_div, 'point_error_message': point_error_message}
			return render(request, 'student/study_plan.html', context)
		else:
			context = {'pre_requisite_units': pre_requisite_unit, 'units': desired_units, 'course_field': course_field,
					   'course_code': course_code, 'semester': semester, 'year': year, 'unit_for_div': unit_for_div,
					   'dict_unit_for_div': dict_unit_for_div, 'point_error_message': point_error_message}
			return render(request, 'student/study_plan.html', context)
def core_unit(request, course_field, course_code, semester, year):
	unit_for_div = []
	unit_codes = SemesterUnit.objects.filter(
		Q(CourseCode=course_code) & Q(Field=course_field.strip()) & Q(Semester=semester)).values('UnitCode')
	desired_units = Unit.objects.filter(Q(UnitCode__in=unit_codes) & Q(Type='CO'))
	pre_requisite_units = PreRequisite.objects.filter(UnitCode__in=unit_codes)
	pre_requisite_unit = [{'UnitCode': pre_requisite.UnitCode, 'PreRequisiteCode': pre_requisite.PreRequisiteCode} for
						  pre_requisite in pre_requisite_units]
	try:
		selected_unit = Unit.objects.get(UnitCode=request.POST['unit'])
		dict_selected_unit = model_to_dict(selected_unit)
		if dict_selected_unit['UnitName'] not in dict_unit_for_div:
			current_unit_point.append(selected_unit.Points)
			if sum(current_unit_point) <= 40:
				dict_unit_for_div[dict_selected_unit['UnitName']] = dict_selected_unit
				unit_for_div.append(selected_unit)
			else:
				del current_unit_point[-1]
				point_error_message = "Total points for current selected unit is " + str(
					sum(current_unit_point)) + "this total can not exceed 40"
	except (KeyError, Unit.DoesNotExist):
		context = {'pre_requisite_units': pre_requisite_unit, 'units': desired_units, 'course_field': course_field,
				   'course_code': course_code, 'semester': semester, 'year': year, 'error_message': "not working"}
		return render(request, 'student/study_plan.html', context)
	else:
		if selected_unit.PreRequisite:
			context = {'pre_requisite_units': pre_requisite_unit, 'units': desired_units, 'course_field': course_field,
					   'course_code': course_code, 'semester': semester, 'year': year, 'unit_for_div': unit_for_div,
					   'dict_unit_for_div': dict_unit_for_div, 'point_error_message': point_error_message}
			return render(request, 'student/study_plan.html', context)
		else:
			context = {'pre_requisite_units': pre_requisite_unit, 'units': desired_units, 'course_field': course_field,
					   'course_code': course_code, 'semester': semester, 'year': year, 'unit_for_div': unit_for_div,
					   'dict_unit_for_div': dict_unit_for_div, 'point_error_message': point_error_message}
			return render(request, 'student/study_plan.html', context)

def research_unit(request, course_field, course_code, semester, year):
	unit_for_div = []
	unit_codes = SemesterUnit.objects.filter(
		Q(CourseCode=course_code) & Q(Field=course_field.strip()) & Q(Semester=semester)).values('UnitCode')
	desired_units = Unit.objects.filter(Q(UnitCode__in=unit_codes) & Q(Type='R'))
	pre_requisite_units = PreRequisite.objects.filter(UnitCode__in=unit_codes)
	pre_requisite_unit = [{'UnitCode': pre_requisite.UnitCode, 'PreRequisiteCode': pre_requisite.PreRequisiteCode} for
						  pre_requisite in pre_requisite_units]
	try:
		selected_unit = Unit.objects.get(UnitCode=request.POST['unit'])
		dict_selected_unit = model_to_dict(selected_unit)
		if dict_selected_unit['UnitName'] not in dict_unit_for_div:
			current_unit_point.append(selected_unit.Points)
			if sum(current_unit_point) <= 40:
				dict_unit_for_div[dict_selected_unit['UnitName']] = dict_selected_unit
				unit_for_div.append(selected_unit)
			else:
				del current_unit_point[-1]
				point_error_message = "Total points for current selected unit is " + str(
					sum(current_unit_point)) + "this total can not exceed 40"
	except (KeyError, Unit.DoesNotExist):
		context = {'pre_requisite_units': pre_requisite_unit, 'units': desired_units, 'course_field': course_field,
				   'course_code': course_code, 'semester': semester, 'year': year, 'error_message': "not working"}
		return render(request, 'student/study_plan.html', context)
	else:
		if selected_unit.PreRequisite:
			context = {'pre_requisite_units': pre_requisite_unit, 'units': desired_units, 'course_field': course_field,
					   'course_code': course_code, 'semester': semester, 'year': year, 'unit_for_div': unit_for_div,
					   'dict_unit_for_div': dict_unit_for_div, 'point_error_message': point_error_message}
			return render(request, 'student/study_plan.html', context)
		else:
			context = {'pre_requisite_units': pre_requisite_unit, 'units': desired_units, 'course_field': course_field,
					   'course_code': course_code, 'semester': semester, 'year': year, 'unit_for_div': unit_for_div,
					   'dict_unit_for_div': dict_unit_for_div, 'point_error_message': point_error_message}
			return render(request, 'student/study_plan.html', context)

def specialist_elective(request, course_field, course_code, semester, year):
	unit_for_div = []
	unit_codes = SemesterUnit.objects.filter(
		Q(CourseCode=course_code) & Q(Field=course_field.strip()) & Q(Semester=semester)).values('UnitCode')
	desired_units = Unit.objects.filter(Q(UnitCode__in=unit_codes) & Q(Type='SE'))
	pre_requisite_units = PreRequisite.objects.filter(UnitCode__in=unit_codes)
	pre_requisite_unit = [{'UnitCode': pre_requisite.UnitCode, 'PreRequisiteCode': pre_requisite.PreRequisiteCode} for
						  pre_requisite in pre_requisite_units]
	try:
		selected_unit = Unit.objects.get(UnitCode=request.POST['unit'])
		dict_selected_unit = model_to_dict(selected_unit)
		if dict_selected_unit['UnitName'] not in dict_unit_for_div:
			current_unit_point.append(selected_unit.Points)
			if sum(current_unit_point) <= 40:
				dict_unit_for_div[dict_selected_unit['UnitName']] = dict_selected_unit
				unit_for_div.append(selected_unit)
			else:
				del current_unit_point[-1]
				point_error_message = "Total points for current selected unit is " + str(
					sum(current_unit_point)) + "this total can not exceed 40"
	except (KeyError, Unit.DoesNotExist):
		context = {'pre_requisite_units': pre_requisite_unit, 'units': desired_units, 'course_field': course_field,
				   'course_code': course_code, 'semester': semester, 'year': year, 'error_message': "not working"}
		return render(request, 'student/study_plan.html', context)
	else:
		if selected_unit.PreRequisite:
			context = {'pre_requisite_units': pre_requisite_unit, 'units': desired_units, 'course_field': course_field,
					   'course_code': course_code, 'semester': semester, 'year': year, 'unit_for_div': unit_for_div,
					   'dict_unit_for_div': dict_unit_for_div, 'point_error_message': point_error_message}
			return render(request, 'student/study_plan.html', context)
		else:
			context = {'pre_requisite_units': pre_requisite_unit, 'units': desired_units, 'course_field': course_field,
					   'course_code': course_code, 'semester': semester, 'year': year, 'unit_for_div': unit_for_div,
					   'dict_unit_for_div': dict_unit_for_div, 'point_error_message': point_error_message}
			return render(request, 'student/study_plan.html', context)

def final_study_plan(request, course_field, course_code, semester, year):
	context = {'final_units' : unit_for_div, 'course_field': course_field, 'course_code': course_code, 'semester': semester, 'year':year}
	return render(request, 'student/final_study_plan.html', context)



