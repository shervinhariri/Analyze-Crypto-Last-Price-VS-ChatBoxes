from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    #return HttpResponse('<h1>THIS IS SHERVIN BLOG</h1>')
    return render(request,"blog/home.html")