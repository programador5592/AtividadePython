import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    now = datetime.datetime.now()
    html = '<html><body>A data atual é %s.<body><html>:' %now
    return HttpResponse(html)

def home2(request):
    return render(request, 'produtos/home.html')
