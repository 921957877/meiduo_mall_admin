from rest_framework.viewsets import ModelViewSet

from meiduo_admin.pages import MyPage
from meiduo_admin.serializers.order_serializer import OrderInfoSerializer, OrderInfoDetailSerializer
from orders.models import OrderInfo


class OrderInfoView(ModelViewSet):
    queryset = OrderInfo.objects.all()
    serializer_class = OrderInfoSerializer
    pagination_class = MyPage

    def get_queryset(self):
        keyword = self.request.query_params.get('keyword')
        if keyword:
            return self.queryset.filter(order_id__contains=keyword)
        return self.queryset.all()

    # 重写get_serializer_class方法,根据不同的action动作,选择不同的序列化器
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return OrderInfoDetailSerializer
        else:
            return self.serializer_class
