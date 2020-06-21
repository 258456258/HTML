# -*- coding: utf-8 -*-


from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("1st URL.........")

def index1(request):
    return HttpResponse('2nd URL...........')    

def index2(request):
	return HttpResponse('3rd URL.............')
