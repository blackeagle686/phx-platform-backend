from rest_framework import serializers
from .models import Service, ServiceMedia, ServiceRequest, CustomServiceRequest, CustomServiceRequestMedia

class ServiceMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceMedia
        fields = ['id', 'image']

class ServiceSerializer(serializers.ModelSerializer):
    media = ServiceMediaSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = ['id', 'title', 'description', 'cover_image', 'media', 'created_at', 'updated_at']

class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = '__all__'

class CustomServiceRequestMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomServiceRequestMedia
        fields = ['id', 'image', 'document']

class CustomServiceRequestSerializer(serializers.ModelSerializer):
    media = CustomServiceRequestMediaSerializer(many=True, read_only=True)
    
    class Meta:
        model = CustomServiceRequest
        fields = '__all__'
