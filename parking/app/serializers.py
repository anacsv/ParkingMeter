from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from app.models import ParkingMeter, Damage


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'password', 'is_active', 'last_login','is_superuser']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'], validated_data['username'])
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        
        if 'password' in validated_data:
            instance.password = make_password(validated_data['password'], validated_data['username'])
        
        user =  self.context['request'].user
        errors = []
        if user.is_superuser:
            is_superuser = validated_data.get('is_superuser', instance.is_superuser)
            if not is_superuser and instance.is_superuser:
                total_superuser = User.objects.filter(is_superuser = True).count()
                if total_superuser > 1:
                    instance.is_superuser = is_superuser
                else:
                    errors.append({"is_superuser": "You cant't not change the last super user"})
            else:
                instance.is_superuser = is_superuser

            if errors:
                raise serializers.ValidationError(errors)    

        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        instance.save()
        return instance


class ParkingMeterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingMeter
        fields = ['id', 'address', 'lon', 'lat']


class DamageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Damage 
        fields = ['id', 'created_at', 'fixed', 'description', 'assigned_user']
