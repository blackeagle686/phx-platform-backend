from django.contrib import admin

# Register your models here.
from .models import Project, ProjectMedia

class ProjectMediaInline(admin.TabularInline):
    model = ProjectMedia
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectMediaInline]
    list_display = ('title', 'created_at', 'updated_at')
