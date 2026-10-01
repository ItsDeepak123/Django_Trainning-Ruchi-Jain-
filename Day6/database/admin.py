from django.contrib import admin
from database.models import Client,Subject,Product 
# Register your models here.
admin.site.register(Client)
admin.site.register(Subject)
admin.site.register(Product)