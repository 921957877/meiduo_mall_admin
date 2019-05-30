from django.contrib.auth.models import Group, Permission
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from meiduo_admin.pages import MyPage
from meiduo_admin.serializers.group_serializer import GroupSerializer, PermissionSimpleSerializer


class GroupView(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = MyPage


class PermissionSimpleView(ListAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSimpleSerializer
