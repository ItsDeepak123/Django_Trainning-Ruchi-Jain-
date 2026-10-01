from django.urls import path
from .views import *
urlpatterns=[
    path('home/',home,name='home'),
    path('Signup/',Signup,name='Signup'),
    path('saveuser/',saveuser,name='saveuser'),
    path('login1/',login1,name='login1'),
    path('loginvalidation/',loginvalidation,name='loginvalidation'),
    path('logout/',logout,name='logout'),
    path('studentregister/',studentregister,name='studentregister'),
    path('studentsave/',studentsave,name='studentsave'),
    path('msg/',msg,name="msg"),


]