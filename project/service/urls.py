from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, ServiceRequestViewSet, CustomServiceRequestViewSet

router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'service-requests', ServiceRequestViewSet, basename='service-request')
router.register(r'custom-requests', CustomServiceRequestViewSet, basename='custom-request')

urlpatterns = [
    path('', include(router.urls)),
]
