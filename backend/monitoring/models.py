from django.db import models
from django.contrib.auth.models import User

class Site(models.Model):
    """Representa una sede/ubicación física"""
    STATUS_CHOICES = [
        ('up', 'Operacional'),
        ('warning', 'Advertencia'),
        ('down', 'Inactivo'),
        ('unknown', 'Desconocido'),
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='España')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    
    # Información de red
    ip_range = models.CharField(max_length=100, blank=True, help_text="Ej: 192.168.1.0/24")
    vlan_id = models.IntegerField(null=True, blank=True)
    
    # Estado
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='unknown')
    last_check = models.DateTimeField(null=True, blank=True)
    
    # Contactos
    contact_name = models.CharField(max_length=100, blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    contact_email = models.EmailField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} ({self.get_status_display()})"

class NetworkDevice(models.Model):
    """Dispositivo de red (router, switch, firewall)"""
    DEVICE_TYPES = [
        ('router', 'Router'),
        ('switch', 'Switch'),
        ('firewall', 'Firewall'),
        ('access_point', 'Access Point'),
        ('server', 'Servidor'),
        ('other', 'Otro'),
    ]
    
    name = models.CharField(max_length=200)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='devices')
    device_type = models.CharField(max_length=50, choices=DEVICE_TYPES)
    ip_address = models.GenericIPAddressField()
    snmp_community = models.CharField(max_length=100, blank=True)
    vendor = models.CharField(max_length=100, blank=True)
    model = models.CharField(max_length=100, blank=True)
    serial_number = models.CharField(max_length=100, blank=True)
    
    # Estado
    is_monitored = models.BooleanField(default=True)
    last_seen = models.DateTimeField(null=True, blank=True)
    
    # Métricas importantes
    cpu_usage = models.FloatField(null=True, blank=True)
    memory_usage = models.FloatField(null=True, blank=True)
    uptime = models.BigIntegerField(null=True, blank=True, help_text="Uptime en segundos")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} ({self.ip_address})"

class Metric(models.Model):
    """Métrica recogida de un dispositivo"""
    METRIC_TYPES = [
        ('cpu', 'Uso de CPU'),
        ('memory', 'Uso de Memoria'),
        ('bandwidth', 'Ancho de Banda'),
        ('latency', 'Latencia'),
        ('packet_loss', 'Pérdida de Paquetes'),
        ('temperature', 'Temperatura'),
        ('interface_status', 'Estado de Interfaz'),
    ]
    
    device = models.ForeignKey(NetworkDevice, on_delete=models.CASCADE, related_name='metrics')
    metric_type = models.CharField(max_length=50, choices=METRIC_TYPES)
    value = models.FloatField()
    unit = models.CharField(max_length=20, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['device', 'metric_type', '-timestamp']),
        ]
    
    def __str__(self):
        return f"{self.device.name} - {self.get_metric_type_display()}: {self.value}{self.unit}"

class Alert(models.Model):
    """Alerta generada por el sistema"""
    SEVERITY_CHOICES = [
        ('info', 'Informativa'),
        ('warning', 'Advertencia'),
        ('critical', 'Crítica'),
    ]
    
    STATUS_CHOICES = [
        ('active', 'Activa'),
        ('acknowledged', 'Reconocida'),
        ('resolved', 'Resuelta'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    
    # Relaciones
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True, blank=True)
    device = models.ForeignKey(NetworkDevice, on_delete=models.CASCADE, null=True, blank=True)
    
    # Metadatos
    detected_at = models.DateTimeField(auto_now_add=True)
    acknowledged_at = models.DateTimeField(null=True, blank=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    acknowledged_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='acknowledged_alerts')
    
    class Meta:
        ordering = ['-detected_at']
    
    def __str__(self):
        return f"[{self.get_severity_display()}] {self.title}"