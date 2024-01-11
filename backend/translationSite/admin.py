from django.contrib import admin
from .models import *

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
    raw_id_fields = ['user']

@admin.register(project)
class ProjectAdmin(admin.ModelAdmin):
        list_display = ['title', 'author', 'publish']
        list_filter = ['deliverytime', 'publish']
        search_fields = ['title', 'author']
        raw_id_fields = ['author']
        date_hierarchy = 'publish'
        ordering = [ 'publish','deliverytime']




@admin.register(outputAI)
class outputAIAdmin(admin.ModelAdmin):
        list_display = ['title', 'status']
        list_filter = ['status', 'starttime', 'endtime']
        search_fields = ['title','sentenceEN']
        ordering = ['status', 'starttime','endtime']


