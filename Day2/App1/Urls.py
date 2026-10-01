from django.urls import path
from App1 import views
urlpatterns=[
    path('Home/',views.Home),
    path('about/',views.about),
]