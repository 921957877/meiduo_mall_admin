from rest_framework import serializers
from goods.models import SKU, SKUSpecification, GoodsCategory, SPU, SPUSpecification, SpecificationOption


# 自定义序列化器，用来序列化从表数据集SKUSpecification
class SKUSpecSerializer(serializers.ModelSerializer):
    spec_id = serializers.IntegerField(read_only=True)
    option_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = SKUSpecification
        fields = ["spec_id", "option_id"]


# 定义sku的序列化器
class SKUSerializer(serializers.ModelSerializer):
    spu = serializers.StringRelatedField(read_only=True)
    spu_id = serializers.IntegerField()
    category = serializers.StringRelatedField(read_only=True)
    category_id = serializers.IntegerField()

    # 从表的数据集
    specs = SKUSpecSerializer(many=True, read_only=True)

    class Meta:
        model = SKU
        fields = "__all__"

    # def create(self, validated_data):
    # 创建sku对象
    # 创建中间表对象SKUSpecification

    # def update(self, instance, validated_data):
    # 跟新中间表对象SKUSpecification


class GoodsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = ['id', 'name']


class SPUSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SPU
        fields = ['id', 'name']


class SpecOptSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecificationOption
        fields = ['id', 'value']


class SPUSpecSerializer(serializers.ModelSerializer):
    spu = serializers.StringRelatedField(read_only=True)
    spu_id = serializers.IntegerField(read_only=True)

    options = SpecOptSerializer(many=True, read_only=True)

    class Meta:
        model = SPUSpecification
        fields = [
            "id",
            "name",
            "spu",
            "spu_id",
            "options"
        ]
