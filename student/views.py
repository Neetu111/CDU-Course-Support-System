from django.db.models import Q
from django.forms import model_to_dict
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import *
from .models import Unit, Course, CourseMajor, SemesterUnit, PreRequisite


dict_unit_for_div = {}
unit_for_div = []
current_unit_point = []
unit_type_list = ["all"]

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

def add_unit(request, course_field, course_code, semester, year):
	error_message = ""
	unit_codes = SemesterUnit.objects.filter(Q(CourseCode=course_code) & Q(Field=course_field.strip()) & Q(Semester=semester)).values('UnitCode')
	unit_type = unit_type_list[0]
	all_unit = Unit.objects.all()
	if(unit_type=="all"):
		desired_units = Unit.objects.filter(UnitCode__in=unit_codes)
	else:
		desired_units = Unit.objects.filter(Q(UnitCode__in=unit_codes) & Q(Type=unit_type))
	pre_requisite_units = PreRequisite.objects.filter(UnitCode__in=unit_codes)
	pre_requisite_unit = [{'UnitCode': pre_requisite.UnitCode, 'PreRequisiteCode': pre_requisite.PreRequisiteCode} for pre_requisite in pre_requisite_units]
	if(request.POST.get('unit',False)):
		selected_unit = Unit.objects.get(UnitCode=request.POST['unit'])
		dict_selected_unit = model_to_dict(selected_unit)
		if dict_selected_unit['UnitName'] not in dict_unit_for_div:
			current_unit_point.append(selected_unit.Points)
			if sum(current_unit_point) <= 40:
				dict_unit_for_div[dict_selected_unit['UnitName']]=dict_selected_unit
				unit_for_div.append(selected_unit)
			else:
				del current_unit_point[-1]
				error_message = "Total points for current selected unit is "+str(sum(current_unit_point)) + "this total can not exceed 40"
		else:
			error_message = "Unit has already been selected"
		context = {'all_units': all_unit, 'pre_requisite_units': pre_requisite_unit, 'units': desired_units, 'course_field': course_field,
				   'course_code': course_code, 'semester': semester, 'year': year, 'unit_type': unit_type,
				   'unit_for_div': unit_for_div, 'dict_unit_for_div': dict_unit_for_div,
				   'error_message': error_message}
		request.session.set_expiry(12)
		return render(request, 'student/study_plan.html', context)
	else:
		context = {'all_units': all_unit, 'unit_for_div': unit_for_div, 'pre_requisite_units': pre_requisite_unit, 'units': desired_units, 'course_field': course_field,
				   'course_code': course_code, 'semester': semester, 'year': year, 'unit_type': unit_type,
				   'error_message': "No unit has been selected"}
		return render(request, 'student/study_plan.html', context)

def delete_unit(request, course_field, course_code, semester, year):
	error_message = ""
	all_unit = Unit.objects.all()
	unit_codes = SemesterUnit.objects.filter(
		Q(CourseCode=course_code) & Q(Field=course_field.strip()) & Q(Semester=semester)).values('UnitCode')
	unit_type = unit_type_list[0]
	if (unit_type == "all"):
		desired_units = Unit.objects.filter(UnitCode__in=unit_codes)
	else:
		desired_units = Unit.objects.filter(Q(UnitCode__in=unit_codes) & Q(Type=unit_type))
	pre_requisite_units = PreRequisite.objects.filter(UnitCode__in=unit_codes)
	pre_requisite_unit = [{'UnitCode': pre_requisite.UnitCode, 'PreRequisiteCode': pre_requisite.PreRequisiteCode} for
						  pre_requisite in pre_requisite_units]
	if (request.POST.get('div_unit', False)):
		selected_unit = Unit.objects.get(UnitCode=request.POST['div_unit'])
		dict_selected_unit = model_to_dict(selected_unit)
		if dict_selected_unit['UnitName'] in dict_unit_for_div:
			del dict_unit_for_div[dict_selected_unit['UnitName']]
			current_unit_point.remove(selected_unit.Points)
			unit_for_div.remove(selected_unit)
		context = {'all_units': all_unit, 'pre_requisite_units': pre_requisite_unit, 'units': desired_units, 'course_field': course_field,
				   'course_code': course_code, 'semester': semester, 'year': year, 'unit_type': unit_type,
				   'unit_for_div': unit_for_div, 'dict_unit_for_div': dict_unit_for_div,
				   'error_message': error_message}
		return render(request, 'student/study_plan.html', context)
	else:
		context = {'all_units': all_unit, 'unit_for_div': unit_for_div, 'pre_requisite_units': pre_requisite_unit, 'units': desired_units,
				   'course_field': course_field,
				   'course_code': course_code, 'semester': semester, 'year': year, 'unit_type': unit_type,
				   'error_message': "No unit has been selected"}
		return render(request, 'student/study_plan.html', context)

def all_unit(request, course_field, course_code, semester, year):
	del unit_type_list[:]
	unit_type_list.append("all")
	result = get_unit(course_field, course_code, semester, year, unit_type_list[0])
	unit_to_show = result[0]
	desired_units = result[1]
	pre_requisite_unit = result[2]
	all_unit = result[3]
	context = {'all_units': all_unit, 'pre_requisite_units':pre_requisite_unit,'units': desired_units, 'course_field': course_field,
			   'course_code': course_code, 'semester': semester, 'year': year, 'unit_for_div': unit_to_show}
	return render(request, 'student/study_plan.html', context)

def common_unit(request, course_field, course_code, semester, year):
	del unit_type_list[:]
	unit_type_list.append("CU")
	result = get_unit(course_field, course_code, semester, year, unit_type_list[0])
	unit_to_show = result[0]
	desired_units = result[1]
	pre_requisite_unit = result[2]
	all_unit = result[3]
	context = {'all_units': all_unit, 'pre_requisite_units': pre_requisite_unit, 'units': desired_units,
			   'course_field': course_field,
			   'course_code': course_code, 'semester': semester, 'year': year, 'unit_for_div': unit_to_show}
	return render(request, 'student/study_plan.html', context)

def core_unit(request, course_field, course_code, semester, year):
	del unit_type_list[:]
	unit_type_list.append("CO")
	result = get_unit(course_field, course_code, semester, year, unit_type_list[0])
	unit_to_show = result[0]
	desired_units = result[1]
	pre_requisite_unit = result[2]
	all_unit = result[3]
	context = {'all_units': all_unit, 'pre_requisite_units': pre_requisite_unit, 'units': desired_units,
			   'course_field': course_field,
			   'course_code': course_code, 'semester': semester, 'year': year, 'unit_for_div': unit_to_show}
	return render(request, 'student/study_plan.html', context)

def research_unit(request, course_field, course_code, semester, year):
	del unit_type_list[:]
	unit_type_list.append("R")
	result = get_unit(course_field, course_code, semester, year, unit_type_list[0])
	unit_to_show = result[0]
	desired_units = result[1]
	pre_requisite_unit = result[2]
	all_unit = result[3]
	context = {'all_units': all_unit, 'pre_requisite_units': pre_requisite_unit, 'units': desired_units,
			   'course_field': course_field,
			   'course_code': course_code, 'semester': semester, 'year': year, 'unit_for_div': unit_to_show}
	return render(request, 'student/study_plan.html', context)

def specialist_elective(request, course_field, course_code, semester, year):
	del unit_type_list[:]
	unit_type_list.append("SE")
	result = get_unit(course_field, course_code, semester, year, unit_type_list[0])
	unit_to_show = result[0]
	desired_units = result[1]
	pre_requisite_unit = result[2]
	all_unit = result[3]
	context = {'all_units': all_unit, 'pre_requisite_units': pre_requisite_unit, 'units': desired_units,
			   'course_field': course_field,
			   'course_code': course_code, 'semester': semester, 'year': year, 'unit_for_div': unit_to_show}
	return render(request, 'student/study_plan.html', context)


def final_study_plan(request, course_field, course_code, semester, year):
	context = {'final_units' : unit_for_div, 'course_field': course_field, 'course_code': course_code, 'semester': semester, 'year':year}
	return render(request, 'student/final_study_plan.html', context)


def get_unit(course_field, course_code, semester, year, unit_type):
	all_unit = Unit.objects.all()
	unit_codes = SemesterUnit.objects.filter(
		Q(CourseCode=course_code) & Q(Field=course_field.strip()) & Q(Semester=semester)).values('UnitCode')
	pre_requisite_units = PreRequisite.objects.filter(UnitCode__in=unit_codes)
	pre_requisite_unit = [{'UnitCode': pre_requisite.UnitCode, 'PreRequisiteCode': pre_requisite.PreRequisiteCode} for
						  pre_requisite in pre_requisite_units]
	if (unit_type == "all"):
		desired_units = Unit.objects.filter(UnitCode__in=unit_codes)
	else:
		desired_units = Unit.objects.filter(Q(UnitCode__in=unit_codes) & Q(Type=unit_type))
	return (unit_for_div, desired_units, pre_requisite_unit, all_unit)