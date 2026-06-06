from rest_framework import viewsets
from .models import TeamMember
from .serializers import TeamMemberSerializer

class TeamMemberViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows team members to be viewed.
    """
    queryset = TeamMember.objects.all().order_by('-created_at')
    serializer_class = TeamMemberSerializer

