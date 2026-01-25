from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Site, NetworkDevice, Metric, Alert

admin.site.register(Site)
admin.site.register(NetworkDevice)
admin.site.register(Metric)
admin.site.register(Alert)