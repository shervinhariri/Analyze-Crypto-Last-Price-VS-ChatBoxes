from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('<h1>THIS IS MY BLOG</h1>')