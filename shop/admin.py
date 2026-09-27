from django.contrib import admin
from .models import Category, Brand, Sneakers

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass

@admin.register(Sneakers)
class SneakersAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'is_exists')