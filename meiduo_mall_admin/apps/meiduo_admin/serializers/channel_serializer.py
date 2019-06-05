from rest_framework import serializers
from goods.models import GoodsChannel, GoodsChannelGroup, GoodsCategory


class GoodsChannelSerializer(serializers.ModelSerializer):
    """商品频道表的序列化器"""
    category = serializers.StringRelatedField(read_only=True)
    category_id = serializers.IntegerField()
    group = serializers.StringRelatedField(read_only=True)
    group_id = serializers.IntegerField()

    class Meta:
        model = GoodsChannel
        fields = '__all__'


class GoodsChannelGroupSerializer(serializers.ModelSerializer):
    """商品频道组表的序列化器"""

    class Meta:
        model = GoodsChannelGroup
        fields = ['id', 'name']


class GoodsCategorySerializer(serializers.ModelSerializer):
    """商品类别表的序列化器"""
    class Meta:
        model = GoodsCategory
        fields = ['id', 'name']