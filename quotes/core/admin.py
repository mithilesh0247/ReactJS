from django.contrib import admin
from core.models import React
# Register your models here.
class CoreAdmin(admin.ModelAdmin):
    list_display=['name','detail']

admin.site.register(React,CoreAdmin)
