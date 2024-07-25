from django.contrib import admin
from .models import Contact, Profile, Product

admin.site.register([Contact, Profile, Product]) 

