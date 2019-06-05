from rest_framework import serializers
from goods.models import SPU, Brand, GoodsCategory


class SPUSerializer(serializers.ModelSerializer):
    """SPU表的序列化器"""
    brand = serializers.StringRelatedField(read_only=True)
    brand_id = serializers.IntegerField()
    category1_id = serializers.IntegerField()
    category2_id = serializers.IntegerField()
    category3_id = serializers.IntegerField()

    class Meta:
        model = SPU
        fields = '__all__'
        # 反序列化过程不需要传category1,category2,category3
        extra_kwargs = {
            'category1': {'read_only': True},
            'category2': {'read_only': True},
            'category3': {'read_only': True},
        }


class BrandSimpleSerializer(serializers.ModelSerializer):
    """商品品牌表的序列化器"""
    class Meta:
        model = Brand
        fields = ['id', 'name']


class SPUCategorySerializer(serializers.ModelSerializer):
    """商品类别表的序列化器"""
    class Meta:
        model = GoodsCategory
        fields = ['id', 'name']

