from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from meiduo_admin.pages import MyPage
from meiduo_admin.serializers.permission_serializer import PermissionSerializer, ContentTypeSerializer


class PermissionView(ModelViewSet):
    queryset = Permission.objects.all().order_by('id')
    serializer_class = PermissionSerializer
    pagination_class = MyPage


class ContentTypeView(ListAPIView):
    queryset = ContentType.objects.all()
    serializer_class = ContentTypeSerializer
