from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from Student.models import login,newuser
from django.urls import reverse 
# Create your views here.
def home(request):
    return render(request,'main.html')

def Signup(request):
    return render(request,'singup.html')

def saveuser(request):
    user1=login()
    u=login.objects.filter(username=request.POST['username'])
    if not u:
        user1.username = request.POST['username']
        user1.password= request.POST['password']
        user1.name= request.POST['name']
        user1.save()
        return HttpResponseRedirect(reverse('login1'))
    else:
        return render(request,'signup.html',{'errormsg':'UserName Already Exist'} )
def login1(request):
    return render(request,'login.html')

def loginvalidation(request):
    try:
        user1=login.objects.get(username=request.POST['username'],password=request.POST['password'])
        return HttpResponseRedirect(reverse('studentregister'))
    except login.DoesNotExist:
        return render(request,'login.html',{'erg':"Invalid Username or Password"})


def logout(request):
    return HttpResponse('<h1>This is logout Page</h1>')
def studentregister(request):
    return render(request,'student.html')
def studentsave(request):
    user1=newuser()
    u=newuser.objects.filter(sname=request.POST['sname'])
    if not u:
        user1.sname=request.POST['sname']
        user1.sid=request.POST['sid']
        user1.sbranch=request.POST['sbranch']
        user1.save()
        return render(request,'student.html',{'successmsg':'Successfully User Registered'})
    else:
        return render(request,'student.html',{'errormsg':'UserName Already Exist'} )

def msg(request):
    return render(request,'main.html')