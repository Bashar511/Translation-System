from django.contrib import admin
from .models import *

# register tables from db in admin panel
# Organize the display of fild in admin panel

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
    raw_id_fields = ['user']
