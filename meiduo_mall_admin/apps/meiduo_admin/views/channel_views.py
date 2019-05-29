from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from goods.models import GoodsChannel, GoodsChannelGroup, GoodsCategory
from meiduo_admin.pages import MyPage
from meiduo_admin.serializers.channel_serializer import GoodsChannelSerializer, GoodsChannelGroupSerializer, \
    GoodsCategorySerializer


class GoodsChannelView(ModelViewSet):
    queryset = GoodsChannel.objects.all()
    serializer_class = GoodsChannelSerializer
    pagination_class = MyPage

    def get_goodschannelgroup(self, request):
        """获取频道组信息"""
        goodschannelgroup_queryset = GoodsChannelGroup.objects.all()
        gs = GoodsChannelGroupSerializer(goodschannelgroup_queryset, many=True)
        return Response(gs.data)

    def get_goodscategory(self, request):
        """获取一级分类信息"""
        cate_queryset = GoodsCategory.objects.filter(parent=None)
        gs = GoodsCategorySerializer(cate_queryset, many=True)
        return Response(gs.data)
