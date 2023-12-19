from django.contrib import admin
from .models import *


@admin.register(Projelerim)
class  ProjelerimAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active','update_time']
    list_editable = ['is_active']
    # prepopulated_fields = {'slug': ['name']} bu admin panelinde slug otomatik yazmak gereklidir.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active','update_time']
    list_editable = ['is_active']

