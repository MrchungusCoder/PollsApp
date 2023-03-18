from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola mundo con Django!!")