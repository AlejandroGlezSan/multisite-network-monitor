from django.contrib import admin
from .models import Site, NetworkDevice, Metric, Alert


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'country', 'status', 'last_check', 'created_at']
    list_filter = ['status', 'country', 'city']
    search_fields = ['name', 'address', 'city']
    readonly_fields = ['created_at', 'updated_at', 'last_check']


@admin.register(NetworkDevice)
class NetworkDeviceAdmin(admin.ModelAdmin):
    list_display = ['name', 'site', 'device_type', 'ip_address', 'vendor', 'is_monitored', 'last_seen']
    list_filter = ['device_type', 'is_monitored', 'site']
    search_fields = ['name', 'ip_address', 'vendor', 'model', 'serial_number']
    readonly_fields = ['created_at', 'updated_at', 'last_seen']


@admin.register(Metric)
class MetricAdmin(admin.ModelAdmin):
    list_display = ['device', 'metric_type', 'value', 'unit', 'timestamp']
    list_filter = ['metric_type']
    search_fields = ['device__name']
    readonly_fields = ['timestamp']


@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ['title', 'severity', 'status', 'site', 'device', 'detected_at']
    list_filter = ['severity', 'status']
    search_fields = ['title', 'description']
    readonly_fields = ['detected_at', 'acknowledged_at', 'resolved_at']