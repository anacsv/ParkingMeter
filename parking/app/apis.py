from app.models import ParkingMeter, Damage
from django.contrib.auth.models import User
from app.serializers import UserSerializer, ParkingMeterSerializer, DamageSerializer
from rest_framework import viewsets, permissions


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ParkingMeterViewSet(viewsets.ModelViewSet):
    queryset = ParkingMeter.objects.all()
    serializer_class = ParkingMeterSerializer
    permission_classes = [permissions.IsAuthenticated]


class DamageViewSet(viewsets.ModelViewSet):
    queryset = Damage.objects.order_by('created_at')
    serializer_class = DamageSerializer
    permission_classes = [permissions.IsAuthenticated]