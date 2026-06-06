from django.contrib import admin

# Register your models here.
from .models import TeamMember

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'user', 'created_at')
