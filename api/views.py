from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request, a=1):
    #TODO
    return HttpResponse(a)