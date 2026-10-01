from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from Paper.models import Paper
from django.urls import reverse
# Create your views here.
def home(request):
    return render(request,'Home.html')

def Register(request):
    Sname=request.POST['Sname']
    Username=request.POST['Username']
    Pass=request.POST['Pass']
    contact=request.POST['contact']
    res=Paper(Sname=Sname,Username=Username,Pass=Pass,contact=contact)
    res.save()
    return render(request,'registration.html')

def login(request):
    Username = request.POST.get('Username')
    Pass = request.POST.get('Pass')

    user = Paper.objects.filter(Username=Username, Pass=Pass).first()
    if user:
        return render(request, 'login.html')
    return render(request, 'question.html')

def questionpaper(request):
    return render(request,'question.html')

def questionpaper1(request):
    return render(request,'question1.html')

def questionpaper2(request):
    return render(request,'question2.html')

def questionpaper3(request):
    return render(request,'question3.html')

def result(request):
    return render(request,'result.html')


