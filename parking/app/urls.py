from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from app import apis
from app.apis import UserViewSet


user_list = UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

router = routers.DefaultRouter()
router.register(r'parking', apis.ParkingMeterViewSet, 'parking')
router.register(r'damage', apis.DamageViewSet, 'damage')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/users/', user_list),
    path('api/users/<int:pk>', user_detail),
    ]