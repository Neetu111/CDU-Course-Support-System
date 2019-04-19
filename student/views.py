# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    #template = loader.get_template('student/index.html')
    context = 0
    return render(request, 'student/index.html', context)