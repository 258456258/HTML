# -*- coding: utf-8 -*-


from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

'''
def index(request):

    return HttpResponse('''
    #<p>This is my first web page in Django</p><h1>1st URL.........</h1><a href="https://github.com/princetyagi258456"> My Github Profile</a>
#    	<h1> 2nd URL....</h1><a href="https://www.linkedin.com/in/prince-tyagi-962b191a4/">My Linked Profile</a>
def index(request):
	return HttpResponse('''Home<p>This is my first web page in Django</p><a href="http://127.0.0.1:8000/removepunc">link to go removepunc</a><a href="http://127.0.0.1:8000/capitalizefirst">link to go capitalizefirst</a><a href="http://127.0.0.1:8000/newlineremove">link to go newlineremove</a><a href="http://127.0.0.1:8000/spaceremove">link to go spaceremovee</a><a href="http://127.0.0.1:8000/charcount">link to go charcount</a>''')

def removepunc(request):
	return HttpResponse('''removepunc<a href="http://127.0.0.1:8000/">link to go homepage</a>''')

def capfirst(request):
	return HttpResponse('''capitalize first<a href="http://127.0.0.1:8000/">link to go homepage</a>''')

def newlineremove(request):
	return HttpResponse('''newline remove<a href="http://127.0.0.1:8000/">link to go homepage</a>''')

def spaceremove(request):
	return HttpResponse('''space remove<a href="http://127.0.0.1:8000/">link to go homepage</a>''')

def charcount(request):
	return HttpResponse('''char count<a href="http://127.0.0.1:8000/">link to go homepage</a>''')




def index1(request):
    return HttpResponse('2nd URL...........') 

def index2(request):
	return HttpResponse('3rd URL.............')
