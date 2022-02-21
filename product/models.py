from unicodedata import name
from xmlrpc.client import boolean
from django.db import models
from django.forms import ModelChoiceField

class ProductType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    attributes = models.ManyToManyField('Attribute', blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Product Type'
        verbose_name_plural = 'Product Types'

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    assigned_attributes = models.ManyToManyField('AssignedAttribute')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class Attribute(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    type = models.CharField(choices=(('text', 'Text'), ('date', 'Date'), ('boolean', 'Boolean'), ('select', 'Select'), ('multiselect', 'Multi Select')), default='text', max_length=100)
    attribute_value = models.ForeignKey('AttributeValue', on_delete=models.CASCADE, blank=True, null=True)

class AssignedAttribute(models.Model):
    id = models.BigAutoField(primary_key=True)
    attribute_value = models.ForeignKey('AttributeValue', on_delete=models.CASCADE)

class AttributeValue(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    boolean = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Attribute'
        verbose_name_plural = 'Attributes'

