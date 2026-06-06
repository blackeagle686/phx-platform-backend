from django.db import models

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover_image = models.ImageField(upload_to='service_images/', blank=True, null=True)

    def __str__(self):
        return self.title

class ServiceMedia(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='media')
    image = models.ImageField(upload_to='service_images/')

    def __str__(self):
        return f"Image {self.id} for {self.service.title}"

class ServiceRequest(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='requests')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=100, blank=True, null=True)
    contact_method = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.service.title}"

class CustomServiceRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=200)
    technical_brief = models.TextField()
    overall_description = models.TextField()
    contact_method = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class CustomServiceRequestMedia(models.Model):
    custom_service_request = models.ForeignKey(CustomServiceRequest, on_delete=models.CASCADE, related_name='media')
    image = models.ImageField(upload_to='custom_service_request_images/')
    document = models.FileField(upload_to='custom_service_request_documents/', blank=True, null=True)

    def __str__(self):
        return f"Image {self.id} for {self.custom_service_request.name}"