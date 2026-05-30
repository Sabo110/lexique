from django.contrib import admin
from .models import Categorie, Mot


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom']
    search_fields = ['nom']


@admin.register(Mot)
class MotAdmin(admin.ModelAdmin):
    list_display = ['id', 'terme', 'categorie']
    search_fields = ['terme', 'definition']