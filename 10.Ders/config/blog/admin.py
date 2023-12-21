from django.contrib import admin
from .models import *


@admin.register(Houses)
class HousesAdmin(admin.ModelAdmin):
    list_display = ['title','is_active','slug']
    # list_display_links = ['slug','title']
    list_editable = ['is_active']


