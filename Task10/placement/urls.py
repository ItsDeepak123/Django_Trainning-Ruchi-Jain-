from django.urls import path
from .views import *
urlpatterns=[
    path('home/',home,name='home'),
    path('Signup/',Signup,name='Signup'),
    path('saveuser/',saveuser,name='saveuser'),
    path('login1/',login1,name='login1'),
    path('Preduction/',Preduction,name='Preduction'),
    path('result/',result,name="result"),
    path('loginvalidation/',loginvalidation,name='loginvalidation'),


]