from django.contrib import admin
from .models import *

@admin.register(Houses)
class HousesAdmin(admin.ModelAdmin):

    list_display = ['title','is_active','slug']
    # list_display_links = ['slug','title']
    list_editable = ['is_active']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name','position','slug','is_active']
    list_editable = ['is_active']