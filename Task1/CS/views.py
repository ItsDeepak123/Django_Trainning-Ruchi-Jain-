from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def About1(request):
    s="<h1>cs is computer science department  </h1>"
    return HttpResponse(s)
def Information2(request):
    s="<h1>CS is the discipline that studies computers, computation, and automation</h1>"
    return HttpResponse(s)
 