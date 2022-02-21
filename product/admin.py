from django.contrib import admin
from product.models import Product, ProductType, Attribute, AssignedAttribute, AttributeValue

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_type', 'created_at', 'updated_at']
    list_filter = ['product_type', 'created_at', 'updated_at']
    search_fields = ['name', 'product_type__name']

class ProductType(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name']

