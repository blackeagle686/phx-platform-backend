from django.contrib import admin

# Register your models here.
from .models import Service, ServiceMedia, ServiceRequest, CustomServiceRequest, CustomServiceRequestMedia

class ServiceMediaInline(admin.TabularInline):
    model = ServiceMedia
    extra = 1

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = [ServiceMediaInline]
    list_display = ('title', 'created_at', 'updated_at')

class CustomServiceRequestMediaInline(admin.TabularInline):
    model = CustomServiceRequestMedia
    extra = 1

@admin.register(CustomServiceRequest)
class CustomServiceRequestAdmin(admin.ModelAdmin):
    inlines = [CustomServiceRequestMediaInline]
    list_display = ('title', 'name', 'email', 'contact_method', 'created_at')

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('service', 'name', 'email', 'contact_method', 'created_at')
