from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers


class PermissionSerializer(serializers.ModelSerializer):
    """权限表的序列化器"""
    class Meta:
        model = Permission
        fields = ['id', 'name', 'codename', 'content_type']


class ContentTypeSerializer(serializers.ModelSerializer):
    """权限类型的表的序列化器"""
    class Meta:
        model = ContentType
        fields = ['id', 'name']