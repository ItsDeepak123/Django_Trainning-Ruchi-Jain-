from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

def Name(request):
    s="<h1>Deepak Prajapati</h1>" \
    "<h1>AiDS Department"
    return HttpResponse(s)