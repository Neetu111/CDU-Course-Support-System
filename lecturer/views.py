from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from lecturer.forms import *
import requests

def lecturer_login(request):
	form = lecturerForm()
	error_message = ""
	if request.method=="POST":
		form = lecturerForm(request.POST)
		# lecturer_id = request.POST.get('LecturerID')
		name = request.POST.get('Name')
		password = request.POST.get('password')
		# name = Lecturer.objects.get(Name = name)
		user = authenticate(username=name, password=password)
		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect(reverse('lecturer:upload_page', args=[name]))
			else:
				error_message = "User is inactive"
		else:
			form = lecturerForm()
			error_message = "Please enter valid username and password"
	context = {'form': form, 'error_message': error_message}
	return render(request, 'lecturer/lecturer_login.html', context)


def upload_page(request, lecturer_name):
	context = {'lecturer_name':lecturer_name}
	return render(request, 'lecturer/upload_page.html', context)

def show_student_progress_report(request, lecturer_name):
	error_message = ""
	context = {}
	if request.method == 'POST' and request.FILES.get('myfile', False):
		myfile = request.FILES['myfile']
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		uploaded_file_url = fs.url(filename)
		# context['lecturer_id'] = lecturer_id
		context['lecturer_name'] = lecturer_name
		return render(request, 'lecturer/upload_page.html', {
			'uploaded_file_url': uploaded_file_url, 'lecturer_name':lecturer_name
		})
	else:
		error_message = "You have not selected any file to upload"
	context = {'error_message':error_message, 'lecturer_name':lecturer_name}
	return render(request, 'lecturer/upload_page.html', {'error_message':error_message, 'lecturer_name':lecturer_name })

def lecturer_logout(request):
	logout(request)
	return render(request, 'lecturer/lecturer_logout.html')