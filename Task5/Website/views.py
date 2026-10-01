from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def laptop(request):
    return render(request,'Laptop.html')

def city(request):
    return render(request,'city.html')
def main(request):
    return render(request,'Main.html')