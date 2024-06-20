from django.contrib import admin
from .models import *

# register tables from db in admin panel
# Organize the display of fild in admin panel




@admin.register(project1)
class ProjectAdmin(admin.ModelAdmin):
        list_display = ['title', 'author', 'publish']
        list_filter = ['deliverytime', 'publish']
        search_fields = ['title', 'author']
        raw_id_fields = ['author']
        date_hierarchy = 'publish'
        ordering = [ 'publish','deliverytime']



# @admin.register(output_AI1)
# class outputAIAdmin(admin.ModelAdmin):
#         list_display = ['title']
#         search_fields = ['title',]


# @admin.register(processed_output_AI)
# class processed_output_AI_Admin(admin.ModelAdmin):
#         list_display = ['sentenceEN', 'sentenceAR', 'starttime','endtime','status']
#         list_filter = ['starttime', 'sentenceEN']
#         search_fields = ['starttime', 'sentenceEN']
#         ordering = ['starttime']


