from django.db import models

# Create your models here.



class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover_image = models.ImageField(upload_to='project_images/', blank=True, null=True)

    def __str__(self):
        return self.title

class ProjectMedia(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='media')
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return f"Image {self.id} for {self.project.title}"


