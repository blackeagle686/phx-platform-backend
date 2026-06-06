from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework import status
from .models import Service, ServiceRequest, CustomServiceRequest
from .serializers import (
    ServiceSerializer, 
    ServiceRequestSerializer, 
    CustomServiceRequestSerializer
)
from .tasks import process_new_service_request

class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint to list and view available services.
    """
    queryset = Service.objects.all().order_by('-created_at')
    serializer_class = ServiceSerializer

class ServiceRequestViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    API endpoint to create a new standard service request.
    """
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        # Trigger celery background task
        process_new_service_request.delay(instance.id, 'standard')

class CustomServiceRequestViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    API endpoint to create a new custom service request.
    """
    queryset = CustomServiceRequest.objects.all()
    serializer_class = CustomServiceRequestSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        # Trigger celery background task
        process_new_service_request.delay(instance.id, 'custom')

