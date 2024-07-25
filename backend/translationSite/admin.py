from django.contrib import admin
from .models import *

# register tables from db in admin panel
# Organize the display of fild in admin panel

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
        list_display = ['title', 'owner', 'publish']
        list_filter = ['deliverytime', 'publish']
        search_fields = ['title', 'owner']
        raw_id_fields = ['owner']
        date_hierarchy = 'publish'
        ordering = [ 'publish','deliverytime']
