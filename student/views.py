from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import *
from .models import Unit, Course, CourseMajor, SemesterUnit, PreRequisite

def study_plan(request, course_field, course_code):
	course_id = CourseMajor.objects.filter(Q(Field = course_field) | Q(CourseCode=course_code))
	unit_id = SemesterUnit.objects.filter(CourseCode=course_code)
	print(unit_id)
	units = Unit.objects.filter(UnitCode=unit_id)
	# courses = Course.objects.filter(CourseName=course_id)
	# print('5')
	# course_majors = CourseMajor.objects.filter(CourseName = course_id)
	# semester_unit = SemesterUnit.objects.filter(CourseName=course_id)
	# pre_requisite = PreRequisite.objects.all()
	context = {'unit': units}
	return render(request, 'student/study_plan.html', context)

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
		#Unit_Name = SemesterUnit.objects.filter(CourseCode = course_code)
		#units = Unit.objects.all()
		if course_code in model_course_code and field in model_field:
			return HttpResponseRedirect(reverse('student:study_plan', args=[field, course_code]))   #redirect(reverse('study_plan'), course_field=field)
			# courses = Course.objects.filter(CourseCode=course_code)
			# # course_majors = CourseMajor.objects.filter(CourseCode = course_code)
			# semester_unit = SemesterUnit.objects.filter(CourseCode=course_code)
			# pre_requisite = PreRequisite.objects.all()
			# context = {'units': units, 'courses': courses, 'course_majors': course_majors, 'semester_unit': semester_unit,
			# 		   'pre_requisite': pre_requisite}
			# return render(request, 'student/study_plan.html', context)
			#
		else:
			form = CourseForm()		# just for checking
	return render(request, 'student/index.html',{'form': form})



def check_prerequisite(request):
	units = Unit.objects.all()
	courses = Course.objects.all()
	course_majors = CourseMajor.objects.all()
	semester_unit = SemesterUnit.objects.all()
	pre_requisite = PreRequisite.objects.all()
	selected_unit = units.object.filter(pk=request.POST['unit'])
	return HttpResponse(selected_unit)
	# except (KeyError, Unit.DoesNotExist):
	# 	return render(request, 'student/StudyPlan.html', {'error_message':"not working"})
	# else:
	# 	if selected_unit.Prerequisite:
	# 		return HttpResponse(selected_unit)
	# 		# pre_requisite = PreRequisite.objects.filter(UnitCode=selected_unit.UnitCode)
	# 		# return render(request, 'student/StudyPlan.html', {'pre_requisite':pre_requisite, 'unit':units})





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
	else:
		selected_unit.is_added = True
		selected_unit.save()

















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




