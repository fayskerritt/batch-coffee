from django.contrib import admin
from .models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'display_name',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'sku',
        'name',
        'description',
        'bag_size',
        'region',
        'variety',
        'altitude',
        'strength',
        'price',
        'image',
        'image_url',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
