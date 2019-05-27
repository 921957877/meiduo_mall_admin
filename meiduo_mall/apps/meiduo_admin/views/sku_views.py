
from rest_framework.generics import ListAPIView,DestroyAPIView,CreateAPIView,RetrieveAPIView
from rest_framework.viewsets import ModelViewSet
from goods.models import SKU,GoodsCategory,SPUSpecification
from meiduo_admin.serializers.sku_serializer import *
from meiduo_admin.pages import MyPage


# class SKUView(ListAPIView, DestroyAPIView, CreateAPIView, RetrieveAPIView):
class SKUView(ModelViewSet):
    queryset = SKU.objects.all()
    serializer_class = SKUSerializer
    pagination_class = MyPage

    def get_queryset(self):
        # 获得过滤的keyword
        keyword = self.request.query_params.get("keyword")
        if keyword:
            return self.queryset.filter(name__contains=keyword)

        # return self.queryset
        # queryset集： 惰性执行，缓存
        return self.queryset.all()



class GoodsCategoryView(ListAPIView):
    queryset = GoodsCategory.objects.filter(parent_id__gt=37)
    serializer_class = GoodsCategorySerializer



class SPUSimpleView(ListAPIView):
    queryset = SPU.objects.all()
    serializer_class = SPUSimpleSerializer





class SpecsView(ListAPIView):
    queryset = SPUSpecification.objects.all()
    serializer_class = SPUSpecSerializer


    def get_queryset(self):
        # 已知条件书spu的id （主表）
        # 查询目标：SPUSpecificaiton（从表）
        pk = self.kwargs.get("pk")
        spuspec_queryset = SPUSpecification.objects.filter(spu_id=pk)

        return spuspec_queryset
















