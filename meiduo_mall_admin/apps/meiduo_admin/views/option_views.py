from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from goods.models import SpecificationOption, SPUSpecification
from goods.views import ListView
from meiduo_admin.pages import MyPage
from meiduo_admin.serializers.option_serializer import SpecOptSerializer, SPUSpecSimpleSerializer


class SpecOptView(ModelViewSet):
    queryset = SpecificationOption.objects.all()
    serializer_class = SpecOptSerializer
    pagination_class = MyPage


class SPUSpecSimpleView(ListAPIView):
    queryset = SPUSpecification.objects.all()
    serializer_class = SPUSpecSimpleSerializer
