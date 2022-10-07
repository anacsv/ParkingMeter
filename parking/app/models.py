from django.utils import timezone
from django.db import models
from django.conf import settings

class ParkingMeter(models.Model):
    address = models.CharField(max_length=280, null=False)
    lon = models.DecimalField(max_digits=22, decimal_places=16, null=False)
    lat = models.DecimalField(max_digits=22, decimal_places=16, null=False)

class Damage(models.Model):
    parking_meter = models.ForeignKey(ParkingMeter, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)    
    fixed = models.BooleanField()
    description = models.CharField(max_length=280)
    assigned_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  null=True)
