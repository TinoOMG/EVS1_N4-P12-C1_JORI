from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def vista1(request):
	return HttpResponse("<h1>Hola Profe :)</h1>"+"<h2>Pongame una buena nota</h2>")

def vista2(request):
	return HttpResponse("<h1>Chao Mundo</h1>")