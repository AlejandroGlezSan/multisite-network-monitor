from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from monitoring import views

router = DefaultRouter()
router.register(r'sites', views.SiteViewSet)
router.register(r'devices', views.NetworkDeviceViewSet)
router.register(r'metrics', views.MetricViewSet)
router.register(r'alerts', views.AlertViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]