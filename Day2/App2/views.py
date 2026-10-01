from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def linkdin(request):
    s="<h1>This is lindin </h1>"
    return HttpResponse(s)

def Facebook(request):
    s="<h1>This is Faccebook</h1>"
    return HttpResponse(s)