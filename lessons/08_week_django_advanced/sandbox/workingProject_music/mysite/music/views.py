#from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	my_str = "<h1> The Music App's homepage </h1>"
	return HttpResponse(my_str)
