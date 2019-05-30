from django.contrib.auth.models import Group
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from meiduo_admin.pages import MyPage
from meiduo_admin.serializers.admin_serializer import AdminSerializer, GroupSimpleSerializer
from users.models import User


class AdminView(ModelViewSet):
    queryset = User.objects.filter(is_staff=True)
    serializer_class = AdminSerializer
    pagination_class = MyPage


class GroupSimpleView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSimpleSerializer
