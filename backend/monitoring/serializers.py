from rest_framework import serializers
from .models import Site, NetworkDevice, Metric, Alert

class SiteSerializer(serializers.ModelSerializer):
    device_count = serializers.SerializerMethodField()
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = Site
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'last_check']
    
    def get_device_count(self, obj):
        return obj.devices.count()

class NetworkDeviceSerializer(serializers.ModelSerializer):
    site_name = serializers.CharField(source='site.name', read_only=True)
    device_type_display = serializers.CharField(source='get_device_type_display', read_only=True)
    
    class Meta:
        model = NetworkDevice
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'last_seen']

class MetricSerializer(serializers.ModelSerializer):
    device_name = serializers.CharField(source='device.name', read_only=True)
    metric_type_display = serializers.CharField(source='get_metric_type_display', read_only=True)
    
    class Meta:
        model = Metric
        fields = '__all__'

class AlertSerializer(serializers.ModelSerializer):
    site_name = serializers.CharField(source='site.name', read_only=True)
    device_name = serializers.CharField(source='device.name', read_only=True)
    severity_display = serializers.CharField(source='get_severity_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = Alert
        fields = '__all__'
        read_only_fields = ['detected_at', 'acknowledged_at', 'resolved_at', 'acknowledged_by']