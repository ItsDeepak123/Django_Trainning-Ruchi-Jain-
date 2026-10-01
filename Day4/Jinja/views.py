from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def testpaper(request):
    Q="Who is Chapta?"
    a="Suryawanshi"
    b="Patel"
    c="Lodhi"
    d="Mehra"
    context={'Question':Q,'Opt1':a,'Opt2':b,'Opt3':c,'Opt4':d}
    template=loader.get_template('testpaper.html')
    res=template.render(context,request)
    return HttpResponse(res)

def name(request):
    Name="Deepak Prajapati"
    Age="25"
    Dept="Aids"
    context={'Name':Name,'Department':Dept,'Age':Age}
    template=loader.get_template("info.html")
    req=template.render(context,request)
    return HttpResponse(req)

def total(request):
    x="10"
    y="20"
    sum=x+y
    context={'x=':x,'y=':y,'Total=':sum}
    template=loader.get_template('sum.html')
    res=template.render(context,request)
    return HttpResponse(res)

def result(request):
    context={'Name':"Deepak Prjapati"
    ,'Marks':92
    }
    #template=loader.get_template('result.html')
    #res=template.render(context,request)
    return render(request,'result.html',context)


def Voting(request):
    context = {
        'name': 'Deepak',
        'Age': 19
    }

    return render(request, 'voting.html', context)

def Home(request):
    return render(request, 'home.html')

def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html') 