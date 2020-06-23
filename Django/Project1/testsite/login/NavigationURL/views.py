# -*- coding: utf-8 -*-


from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):

    return HttpResponse('''<p>This is my first web page in Django</p><h1>1st URL.........</h1><a href="https://github.com/princetyagi258456"> My Github Profile</a>
    	<h1> 2nd URL....</h1><a href="https://www.linkedin.com/in/prince-tyagi-962b191a4/">My Linked Profile</a>''')


def index1(request):
    return HttpResponse('2nd URL...........')    

def index2(request):
	return HttpResponse('3rd URL.............')
