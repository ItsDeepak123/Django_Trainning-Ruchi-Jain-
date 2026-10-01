from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Home(request):
    s="<h1>Gandhi Nagar Near Airport Road bhopal (M.P.)</h1>"
    return HttpResponse(s)
def Information1(request):
    s="<h1>Established in 1992 under the Ministry of Health & Family Welfare</h1>"
    return HttpResponse(s)  