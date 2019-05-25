from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from lecturer.forms import *
import requests

def lecturer_login(request):
	form = lecturerForm()
	if request.method=="POST":
		form = lecturerForm(request.POST)
		lecturer_id = request.POST.get('LecturerID')
		password = request.POST.get('password')
		lecturers = Lecturer.objects.all()
		model_lecturer_id = []
		model_password = []
		for lecturer in lecturers:
			model_lecturer_id.append(lecturer.LecturerID)
			model_password.append(lecturer.password)
		if lecturer_id in model_lecturer_id and password in model_password:
			lecturer = Lecturer.objects.get(LecturerID=lecturer_id)
			print(lecturer.Name)
			return HttpResponseRedirect(reverse('lecturer:upload_page', args=[lecturer_id, lecturer.Name]))
		else:
			form = lecturerForm()
	return render(request, 'lecturer/lecturer_login.html',{'form': form})


def upload_page(request, lecturer_id, lecturer_name):
	context = {'lecturer_id': lecturer_id, 'lecturer_name':lecturer_name}
	return render(request, 'lecturer/upload_page.html', context)
