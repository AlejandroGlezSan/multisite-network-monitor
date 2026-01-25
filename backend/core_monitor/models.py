from django.db import models

# Create your models here.
from django.db import models

class Site(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class NetworkDevice(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Metric(models.Model):
    device = models.ForeignKey(NetworkDevice, on_delete=models.CASCADE)
    metric_type = models.CharField(max_length=50)
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.device.name} - {self.metric_type}"

class Alert(models.Model):
    device = models.ForeignKey(NetworkDevice, on_delete=models.CASCADE)
    alert_type = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.device.name} - {self.alert_type}"