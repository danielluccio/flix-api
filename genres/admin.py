from django.contrib import admin
from .models import Genre

@admin.register(Genre)
class AdminGenre(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
