from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from rest_framework import serializers

from users.models import User


class AdminSerializer(serializers.ModelSerializer):
    """管理员的序列化器"""

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'mobile', 'password', 'groups', 'user_permissions']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    # 重写create方法使密码能够加密,用户变为超级管理员
    def create(self, validated_data):
        password = validated_data['password']
        validated_data['password'] = make_password(password)
        validated_data['is_staff'] = True
        return super().create(validated_data)


class GroupSimpleSerializer(serializers.ModelSerializer):
    """用户组简单信息的序列化器"""

    class Meta:
        model = Group
        fields = ['id', 'name']
