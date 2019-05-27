from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from goods.models import SPU, Brand, GoodsCategory
from meiduo_admin.pages import MyPage
from meiduo_admin.serializers.spu_serializer import SPUSerializer, BrandSimpleSerializer, SPUCategorySerializer


class SPUView(ModelViewSet):
    queryset = SPU.objects.all()
    serializer_class = SPUSerializer
    pagination_class = MyPage

    # def get_queryset(self):
    #     keyword = self.request.query_params.get('keyword')
    #     if keyword:
    #         return self.queryset.filter(name__contains=keyword)
    #     return self.queryset.all()


class BrandSimpleView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSimpleSerializer


class SPUCategoryView(ListAPIView):
    queryset = GoodsCategory.objects.all()
    serializer_class = SPUCategorySerializer

    # 重写get_queryset方法,通过判断是否有pk来决定是一级分类还是二三级分类数据
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk:
            return self.queryset.filter(parent_id=pk)
        return self.queryset.filter(parent=None)
