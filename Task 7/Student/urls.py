from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('students/', views.studentlist, name='studentlist'),
    path('update/', views.update_student, name='update_student'),
    path('delete/', views.delete_student, name='delete_student'),
]