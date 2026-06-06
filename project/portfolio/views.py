from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer
from project.permissions import IsAdminUserOrReadOnly

class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed and edited by admin.
    """
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminUserOrReadOnly]
