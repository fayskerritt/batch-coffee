from django.contrib import admin
from .models import Product, Category, Variety


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'display_name',
    )


class VarietyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'display_name',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category', 'variety', 'sku', 'name',
        'description', 'bag_size', 'region',
        'altitude', 'strength', 'price', 'image',
        'image_url',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Variety, VarietyAdmin)
admin.site.register(Product, ProductAdmin)
