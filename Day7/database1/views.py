from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from database1.models import employee
from django.urls import reverse
# Create your views here.
def newemployeeform(request):
    res=render(request,"form.html")
    return res
def saveuser(request):  # create recored (c for crud)
    eno=request.POST['eno'] 
    ename=request.POST['ename']
    esal=request.POST['esal']
    emp=employee(eno=eno,ename=ename,esal=esal)
    emp.save()
    url=reverse('employeelist')
    return HttpResponseRedirect(url)

def employeelist(request):      
    employees=employee.objects.all()     
    res=render(request,'employeelist.html',{'employees':employees})  #Read data recordes(r of crud)
    return res       

def update_employeeform(request):
    id=request.GET['id']
    emp=employee.objects.filter(id=id).values()
    res=render(request,'updateemployeeform.html',{'employee':emp[0]})
    return res                            #it return queryset of employee

def update_employee(request):
    id=request.POST['id']
    eno=request.POST['eno'] 
    ename=request.POST['ename']
    esal=request.POST['esal']
    employee(eno=eno,ename=ename,esal=esal).save()
    url=reverse('employeelist')
    return HttpResponseRedirect(url)

def delete_employee(request):
    id=request.GET['id']
    emp=employee.objects.filter(id=id)
    emp.delete()
    url=reverse('employeelist')
    return HttpResponseRedirect(url)