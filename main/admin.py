from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image'] # показ
    list_display_links = ['name'] # ссылки
    list_per_page = 5 # кол-во записей на одной странице
    search_fields = ['name'] # поисковая строка


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'category',] # показ
    list_display_links = ['category','name', 'price'] # ссылки
    ordering = ['price'] #фильтр
    list_per_page = 5  #кол-во записей на одной странице
    search_fields = ['name', 'price']  # поисковая строка

#admin.site.register(Category, CategoryAdmin)
#admin.site.register(Subject, SubjectAdmin)


