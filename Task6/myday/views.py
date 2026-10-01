from django.shortcuts import render
from django.http import HttpResponseRedirect
from myday.models import Product
from django.urls import reverse


# Create all products with one click
def newproduct(request):
    res=render(request,'newproduct.html')
    return res

def saveorder(request):
    Product(pname="Dove Soap", pprice=40, poffer=10).save()
    Product(pname="Dove Shampoo", pprice=400, poffer=10).save()
    Product(pname="Bellaweta Perfume", pprice=1000, poffer=10).save()
    Product(pname="Chaipatti", pprice=1000, poffer=10).save()
    Product(pname="Parle-G", pprice=10, poffer=10).save()
    Product(pname="Chawal", pprice=1000, poffer=10).save()
    Product(pname="Dal", pprice=1000, poffer=10).save()
    pname=request.POST['pname']
    pprice=request.POST['pprice']
    poffer=request.POST['poffer']
    emp= Product(pname=pname,pprice=pprice,poffer=poffer)
    emp.save()
    url=reverse('productlist')
    return HttpResponseRedirect(url)
    
    return productlist(request) 


# Read all products
def productlist(request):
    product = Product.objects.all()
    return render(request, 'product.html', {'product': product})


# Update product
def updateProduct(request):
    id = 1
    pname = "dettol"
    pprice = 55
    poffer = 60
    Product(id=id, pname=pname, pprice=pprice, poffer=poffer).save()
    id = 42
    pname = "burbourne"
    pprice = 55
    poffer = 60
    Product(id=id, pname=pname, pprice=pprice, poffer=poffer).save()
    return productlist(request)


# Delete product
def deleteProduct(request):
    id = 1
    pmp = Product.objects.filter(id=id)
    pmp.delete()
    return productlist(request)