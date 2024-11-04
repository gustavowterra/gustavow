from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.
class CustomUserAdmin(UserAdmin):
    pass

admin.site.register (Empresa)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)