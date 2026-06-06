from rest_framework import serializers
from .models import Project, ProjectMedia

class ProjectMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMedia
        fields = ['id', 'image']

class ProjectSerializer(serializers.ModelSerializer):
    media = ProjectMediaSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'cover_image', 'media', 'created_at', 'updated_at']
