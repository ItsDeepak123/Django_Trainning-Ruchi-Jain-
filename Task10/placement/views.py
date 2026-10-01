from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from placement.models import registration
from django.urls import reverse
import joblib 
def home(request):
    return render(request,'home.html')

def Signup(request):
    return render(request,'signup.html')
    

def saveuser(request):
    user1=registration()
    u=registration.objects.filter(username=request.POST['username'])
    if not u:
        user1.username=request.POST['username']
        user1.password=request.POST['password']
        user1.sname=request.POST['sname']
        user1.scontact=request.POST['scontact']
        user1.sid=request.POST['sid']
        user1.semail=request.POST['semail']
        user1.save()
        return HttpResponseRedirect(reverse('login1'))
    else:
        return render(request,'signup',{'errormsg':'UserName Already Exist'} )
def login1(request):
    return render(request,'login.html')
def loginvalidation(request):
    try:
        user1=registration.objects.get(username=request.POST['username'],password=request.POST['password'])
        return HttpResponseRedirect(reverse('Preduction'))
    except registration.DoesNotExist:
        return render(request,'login.html',{'erg':"Invalid Username or Password"})
def Preduction(request):
    return render(request,'preduction.html')

def result(request):
    scaler=joblib.load('scalermodel.pkl')
    mlmodel=joblib.load('mlmodel.pkl')
    cgpa=float(request.GET['cgpa'])
    iq=float(request.GET['iq'])
    profile_score=float(request.GET['profile_score'])
    data=[cgpa,iq,profile_score]
    scaler_input=scaler.transform([data])
    ans=int(mlmodel.predict(scaler_input)[0])
    return render(request,'result.html',{'Answer':ans,'CGPA':cgpa,'Profile_score':profile_score})
