from django.urls import path
from . import views
urlpatterns=[
    path('home/',views.home,name='home'),
    path('Register/',views.Register,name='Register'),
    path('login/',views.login,name='login'),
    path('questionpaper/',views.questionpaper,name='questionpaper'),
    path('questionpaper1/',views.questionpaper1,name='questionpaper1'),
    path('questionpaper2/',views.questionpaper2,name='questionpaper2'),
    path('questionpaper3/',views.questionpaper3,name='questionpaper3'),
    path('result/',views.result,name='result'),

]