from django.urls import include, path
from rest_framework import routers
from product import views


router = routers.DefaultRouter()
router.register(r'producttype', views.ProductTypeViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'attribute', views.AttributeViewSet)
router.register(r'assignedattribute', views.AssignedAttributeViewSet)
router.register(r'attributevalue', views.AttributeValueViewSet)

# Wire up Api using auto URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    
]


