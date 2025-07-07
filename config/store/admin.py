from django.contrib import admin
from .models import Product  # import your Product model

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'stock', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name']
