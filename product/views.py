from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from product.models import AssignedAttribute, Attribute, AttributeValue, Product, ProductType
from product.serializers import ProductTypeSerializer, ProductSerializer, AttributeSerializer, AssignedAttributeSerializer, AttributeValueSerializer

class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class AttributeViewSet(viewsets.ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer

class AssignedAttributeViewSet(viewsets.ModelViewSet):
    queryset = AssignedAttribute.objects.all()
    serializer_class = AssignedAttributeSerializer

class AttributeValueViewSet(viewsets.ModelViewSet):
    queryset = AttributeValue.objects.all()
    serializer_class = AttributeValueSerializer
