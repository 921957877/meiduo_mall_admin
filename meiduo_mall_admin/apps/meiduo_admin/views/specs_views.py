from rest_framework.viewsets import ModelViewSet

from goods.models import SPUSpecification
from meiduo_admin.pages import MyPage
from meiduo_admin.serializers.specs_serializer import SPUSpecSerializer


class SPUSpecView(ModelViewSet):
    queryset = SPUSpecification.objects.all()
    serializer_class = SPUSpecSerializer
    pagination_class = MyPage
