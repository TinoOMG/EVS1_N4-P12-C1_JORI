from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def vista3(request):
	return HttpResponse("<h1>Perritos</h1>"+"<h2>Son Feos</h2>")

def vista4(request):
	return HttpResponse("<h1>Gatitos</h1>"+"<h2>Son Bonitos</h2>"+"<h3>Y suavesitos</h3>")