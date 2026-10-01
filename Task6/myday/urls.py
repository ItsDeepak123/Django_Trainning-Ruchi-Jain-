from django.urls import path 
from . views import * 

urlpatterns=[
    path('saveorder/',saveorder,name='saveuser'),
    path('productlist/',productlist,name='productlist'),
    path('updateproduct/',updateProduct,name='Updateproduct'),
    path('deleteproduct/',deleteProduct,name='deleteProduct,'),
    path('newProduct/', newproduct ,name='newProduct'),
    ]