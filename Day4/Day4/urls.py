"""
URL configuration for Day4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Jinja import views
urlpatterns = [
    # path('result/',views.result),
    # path('Voting/',views.Voting),
    # path('testpaper/',views.testpaper),
    # path('name/',views.name),
    # path('total/',views.total),
    path('',views.Home, name="Home"),
    path('about/',views.About, name="About"),
    path('contact/',views.Contact, name="Contact"),
    path('admin/', admin.site.urls),
]
