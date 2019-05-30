from django.contrib.auth.models import Group, Permission
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    """用户组的序列化器"""

    class Meta:
        model = Group
        fields = ['id', 'name', 'permissions']


class PermissionSimpleSerializer(serializers.ModelSerializer):
    """权限表的简单信息序列化器"""

    class Meta:
        model = Permission
        fields = ['id', 'name']
