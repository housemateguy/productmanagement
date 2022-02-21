from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from product.serializers import ProductType, Product, Attribute, AssignedAttribute, AttributeValue

class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductType
    permission_classes = [permissions.IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = Product
    permission_classes = [permissions.IsAuthenticated]

class AttributeViewSet(viewsets.ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = Attribute
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Attribute.objects.all()
        else:
            return Attribute.objects.filter(user=user)


class AssignedAttributeViewSet(viewsets.ModelViewSet):
    queryset = AssignedAttribute.objects.all()
    serializer_class = AssignedAttribute
    permission_classes = [permissions.IsAuthenticated]

class AttributeValueViewSet(viewsets.ModelViewSet):
    queryset = AttributeValue.objects.all()
    serializer_class = AttributeValue
    permission_classes = [permissions.IsAuthenticated]