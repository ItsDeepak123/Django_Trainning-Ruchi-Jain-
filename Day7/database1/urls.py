from django.urls import path 
from . views import * 

urlpatterns=[
    path('delete_employee/',delete_employee,name='delete_employee'),
    path('saveuser/',saveuser,name='saveuser'),
    path('update_employee/',update_employee,name='update_employee'),
    path('employeelist/',employeelist,name='employeelist'),
    path('newemployeeform/',newemployeeform,name='newemployeeform'),
    path('update_employeeform/',update_employeeform,name='updateemployeeform')

]