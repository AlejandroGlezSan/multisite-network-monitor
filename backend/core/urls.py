# backend/core/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core_monitor import views

router = routers.DefaultRouter()
router.register(r'sites', views.SiteViewSet)
router.register(r'devices', views.NetworkDeviceViewSet)
router.register(r'metrics', views.MetricViewSet)
router.register(r'alerts', views.AlertViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]