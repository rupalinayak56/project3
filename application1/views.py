from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def radhe(request):
    return HttpResponse('<h1><marquee> Hello Guys<marquee></h1>')
def krishna(request):
    return HttpResponse('<h1><marquee> Welcome to World<marquee></h1>')
