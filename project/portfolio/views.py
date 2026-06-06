from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows projects to be viewed.
    """
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer

