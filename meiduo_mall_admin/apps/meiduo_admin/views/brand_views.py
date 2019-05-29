from rest_framework.viewsets import ModelViewSet

from goods.models import Brand
from meiduo_admin.pages import MyPage
from meiduo_admin.serializers.brand_serializer import BrandSerializer


class BrandView(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    pagination_class = MyPage
