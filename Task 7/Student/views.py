from django.shortcuts import render
from django.http import HttpResponse
from Student.models import Student
# Create your views here.
def home(request):
    students=Student.objects.all()
    return render(request, 'main.html',{'Student': students})

def create(request):
    sid=1
    sname="Deepak"
    sbranch="Aids"
    std=Student(sid=sid,sname=sname,sbranch=sbranch)
    std.save()
    students=Student.objects.all()
    return render(request, 'main.html',{'Student': students})

def studentlist(request):
    students=Student.objects.all()
    return render(request, 'main.html',{'Student': students})                                                     #it return queryset of employee

def update_student(request):
    sid=1
    sname="Harsh Chapta"
    sbranch=45854
    Student.objects.filter(sid=sid).update(sname=sname,sbranch=sbranch)
    students=Student.objects.all()
    return render(request, 'main.html',{'Student': students})

def delete_student(request):
    sid=1
    std=Student.objects.filter(sid=sid)
    std.delete()
    students=Student.objects.all()
    return render(request, 'main.html',{'Student': students})