from django.contrib import admin
from .models import Menu, Order


# Registering the Menu and Order models
admin.site.register(Menu)
admin.site.register(Order)