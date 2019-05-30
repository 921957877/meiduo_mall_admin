from rest_framework import serializers

from goods.models import SKU
from orders.models import OrderInfo, OrderGoods


class OrderInfoSerializer(serializers.ModelSerializer):
    """订单信息表的序列化器"""

    class Meta:
        model = OrderInfo
        fields = ['order_id', 'create_time', 'status']
        extra_kwargs = {
            'status': {'write_only': True}
        }


class SKUSimpleSerializer(serializers.ModelSerializer):
    """SKU的简单信息序列化器"""

    class Meta:
        model = SKU
        fields = ['name', 'default_image']


class OrderGoodsSerializer(serializers.ModelSerializer):
    """订单商品表的序列化器"""
    sku = SKUSimpleSerializer(read_only=True)

    class Meta:
        model = OrderGoods
        fields = ['count', 'price', 'sku']


class OrderInfoDetailSerializer(serializers.ModelSerializer):
    """订单详情数据的序列化器"""
    user = serializers.StringRelatedField(read_only=True)
    skus = OrderGoodsSerializer(many=True, read_only=True)

    class Meta:
        model = OrderInfo
        fields = ['order_id', 'user', 'total_count', 'total_amount', 'freight', 'pay_method', 'status', 'create_time',
                  'skus']
