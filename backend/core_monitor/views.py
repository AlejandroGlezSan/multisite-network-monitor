from django.shortcuts import render
from rest_framework import viewsets
from .models import Site, NetworkDevice, Metric, Alert
from .serializers import SiteSerializer, NetworkDeviceSerializer, MetricSerializer, AlertSerializer

class SiteViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite ver o editar las sedes (sites).
    """
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

class NetworkDeviceViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite ver o editar los dispositivos de red (network devices).
    """
    queryset = NetworkDevice.objects.all()
    serializer_class = NetworkDeviceSerializer

class MetricViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite ver o editar las métricas (metrics).
    """
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer

class AlertViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite ver o editar las alertas (alerts).
    """
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer