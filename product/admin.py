from django.contrib import admin
from product.models import Product, ProductType, Attribute, AssignedAttribute, AttributeValue

class Product(admin.ModelAdmin):
    list_display = ['id', 'name']

class ProductType(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

