from rest_framework import serializers
from goods.models import SKU, SKUSpecification, GoodsCategory, SPU, SPUSpecification, SpecificationOption


# 自定义序列化器，用来序列化从表数据集SKUSpecification
class SKUSpecSerializer(serializers.ModelSerializer):
    spec_id = serializers.IntegerField()
    option_id = serializers.IntegerField()

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
    specs = SKUSpecSerializer(many=True)

    # 重写create方法,使保存sku时sku的规格和选项也进行保存
    def create(self, validated_data):
        # 提取规格和选项信息  specs: [{spec_id: "4", option_id: 8}, {spec_id: "5", option_id: 11}]
        specs = validated_data.pop('specs')
        # 创建sku对象
        sku = self.Meta.model.objects.create(**validated_data)
        # 遍历规格和选项信息,逐个进行保存
        for i in specs:
            # {spec_id: "5", option_id: 11}
            # 拼接SKUSpecification中间表的数据
            i['sku_id'] = sku.id
            SKUSpecification.objects.create(**i)
        return sku

    # 重写update方法,使更新sku时sku的规格和选项也进行更新
    def update(self, instance, validated_data):
        # 提取规格和选项信息  specs: [{spec_id: "4", option_id: 8}, {spec_id: "5", option_id: 11}]
        specs = validated_data.pop('specs')
        # 遍历规格和选项信息,逐个进行更新
        for i in specs:
            # {spec_id: "4", option_id: 8}
            # 根据sku_id和spec_id获得唯一的一条信息进行更新
            skuspecification = SKUSpecification.objects.get(sku_id=instance.id, spec_id=i.get('spec_id'))
            skuspecification.option_id = i.get('option_id')
            skuspecification.save()
        return instance

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
