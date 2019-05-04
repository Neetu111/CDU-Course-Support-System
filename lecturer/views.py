from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.core.context_processors import csrf


def index(request):
     return HttpResponse("<h1>Working</h1>")
