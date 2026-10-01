from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from myuser.models import user
from django.urls import reverse 
# Create your views here.
def home(request):
    return render(request,'main.html')

def Signup(request):
    # return render(request,'singup.html')
    return HttpResponse("<h1>This is signup page</h1>")

def saveuser(request):
    user1=user()
    u=user.objects.filter(username=request.POST['username'])
    if not u:
        user1.usernane=request.POST['username']
        user1.password=request.POST['password']
        user1.name=request.POST['name']
        user1.contact=request.POST['contact']
        user1.save()
        return HttpResponseRedirect(reverse('login'))
    else:
        return render(request,'singup.html',{'errormsg':'UserName Already Exist'} )
def login(request):
    return render(request,'login.html')

def loginvalidation(request):
    try:
        user1=user.objects.get(username=request.POST['username']
                               ,password=request.POST['password'])
         #session create
        request.session['username']=user1.username
        request.session['name']=user1.name
        return HttpResponseRedirect(reverse('home'))
    except user.DoesNotExist:
        return render(request,'login.html',{'erg':"Invalid Username or Password"})
   


def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('login'))
