from django.urls import path
from App2 import views
urlpatterns=[
    path('linkdin/',views.linkdin),
    path('Facebook/',views.Facebook),
]