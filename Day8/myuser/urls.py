from django.urls import path
from . import views


urlpatterns=[
    path('Home/',views.home,name='Home'),
    path('Signup/',views.Signup,name='Signup'),
    path('saveuser/',views.saveuser,name='saveuser'),
    path('login/',views.login,name='login'),
    path('loginvalidation/',views.loginvalidation,name='loginvalidation'),
    path('logout/',views.logout,name='logout'),



] 