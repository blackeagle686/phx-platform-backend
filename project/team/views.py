from rest_framework import viewsets
from .models import TeamMember
from .serializers import TeamMemberSerializer
from project.permissions import IsAdminUserOrReadOnly

class TeamMemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows team members to be viewed and edited by admin.
    """
    queryset = TeamMember.objects.all().order_by('-created_at')
    serializer_class = TeamMemberSerializer
    permission_classes = [IsAdminUserOrReadOnly]
