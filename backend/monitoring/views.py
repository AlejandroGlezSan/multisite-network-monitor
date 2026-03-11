from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import Site, NetworkDevice, Metric, Alert
from .serializers import SiteSerializer, NetworkDeviceSerializer, MetricSerializer, AlertSerializer


class SiteViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gestionar sedes (sites).
    Soporta filtrado por status y ordenación.
    """
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'city', 'address']
    ordering_fields = ['name', 'status', 'created_at']

    @action(detail=True, methods=['get'])
    def devices(self, request, pk=None):
        """Devuelve los dispositivos asociados a una sede."""
        site = self.get_object()
        devices = site.devices.all()
        serializer = NetworkDeviceSerializer(devices, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def alerts(self, request, pk=None):
        """Devuelve las alertas activas de una sede."""
        site = self.get_object()
        alerts = Alert.objects.filter(site=site, status='active')
        serializer = AlertSerializer(alerts, many=True)
        return Response(serializer.data)


class NetworkDeviceViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gestionar dispositivos de red.
    """
    queryset = NetworkDevice.objects.select_related('site').all()
    serializer_class = NetworkDeviceSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'ip_address', 'vendor', 'model']
    ordering_fields = ['name', 'device_type', 'created_at']

    def get_queryset(self):
        qs = super().get_queryset()
        site_id = self.request.query_params.get('site')
        device_type = self.request.query_params.get('type')
        if site_id:
            qs = qs.filter(site_id=site_id)
        if device_type:
            qs = qs.filter(device_type=device_type)
        return qs

    @action(detail=True, methods=['get'])
    def metrics(self, request, pk=None):
        """Devuelve las últimas métricas de un dispositivo."""
        device = self.get_object()
        limit = int(request.query_params.get('limit', 50))
        metrics = device.metrics.all()[:limit]
        serializer = MetricSerializer(metrics, many=True)
        return Response(serializer.data)


class MetricViewSet(viewsets.ModelViewSet):
    """
    API endpoint para métricas de dispositivos.
    """
    queryset = Metric.objects.select_related('device').all()
    serializer_class = MetricSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['timestamp', 'value']

    def get_queryset(self):
        qs = super().get_queryset()
        device_id = self.request.query_params.get('device')
        metric_type = self.request.query_params.get('type')
        if device_id:
            qs = qs.filter(device_id=device_id)
        if metric_type:
            qs = qs.filter(metric_type=metric_type)
        return qs


class AlertViewSet(viewsets.ModelViewSet):
    """
    API endpoint para alertas del sistema.
    """
    queryset = Alert.objects.select_related('site', 'device', 'acknowledged_by').all()
    serializer_class = AlertSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['detected_at', 'severity', 'status']

    def get_queryset(self):
        qs = super().get_queryset()
        status = self.request.query_params.get('status')
        severity = self.request.query_params.get('severity')
        if status:
            qs = qs.filter(status=status)
        if severity:
            qs = qs.filter(severity=severity)
        return qs

    @action(detail=True, methods=['post'])
    def acknowledge(self, request, pk=None):
        """Marca una alerta como reconocida."""
        alert = self.get_object()
        alert.status = 'acknowledged'
        alert.acknowledged_at = timezone.now()
        alert.acknowledged_by = request.user if request.user.is_authenticated else None
        alert.save()
        return Response({'status': 'acknowledged', 'id': alert.id})

    @action(detail=True, methods=['post'])
    def resolve(self, request, pk=None):
        """Marca una alerta como resuelta."""
        alert = self.get_object()
        alert.status = 'resolved'
        alert.resolved_at = timezone.now()
        alert.save()
        return Response({'status': 'resolved', 'id': alert.id})