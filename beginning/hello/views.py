from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Hello, World")

def brian(request):
    return HttpResponse("Hello, Brian!")

def suleiman(request):
    return HttpResponse("Hello, Suleiman")
    

def greet(request, name):
    return HttpResponse(f"hello, {name}")