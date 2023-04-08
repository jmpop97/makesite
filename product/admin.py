from django.contrib import admin
from .models import Products

class TimeDisplay(admin.ModelAdmin):
    list_display = ('producter','name','description','prise','amount','size','created_at','updated_at')
    fields =('producter','name','description','prise','amount','size','created_at','updated_at')
    readonly_fields = ('created_at','updated_at')

# Register your models here.
admin.site.register(Products,TimeDisplay)