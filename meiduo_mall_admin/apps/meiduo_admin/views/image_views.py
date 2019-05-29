from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from goods.models import SKUImage, SKU
from meiduo_admin.pages import MyPage
from meiduo_admin.serializers.image_serializer import SKUImageSerializer, SKUSimpleSerializer


class SKUImageView(ModelViewSet):
    queryset = SKUImage.objects.all()
    serializer_class = SKUImageSerializer
    pagination_class = MyPage


class SKUSimpleView(ListAPIView):
    queryset = SKU.objects.all()
    serializer_class = SKUSimpleSerializer
