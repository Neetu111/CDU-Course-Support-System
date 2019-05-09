from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.core.context_processors import csrf
from lecturer.forms import *
import requests


def index(request):
	form = lecturerForm()
	if request.method=="POST":
		form = lecturerForm(request.POST)
		lecturerid = request.POST.get('LecturerID')
		password = request.POST.get('password')
		lecturers = Lecturer.objects.all()
		model_lecturer_id = []
		model_password = []
		for lecturer in lecturers:
			model_lecturer_id.append(lecturer.LecturerID)
			model_password.append(lecturer.password)
		if lecturerid in model_lecturer_id and password in model_password:
			return render(request, 'lecturer/uploadpage.html')
		else:
			return HttpResponse(form.is_valid())
	return render(request, 'lecturer/lecturerlogin.html', {'form': form})
    #return redirect('UploadPage')


def UploadPage(request):
    #context = 0
    return render(request, 'lecturer/uploadpage.html')
