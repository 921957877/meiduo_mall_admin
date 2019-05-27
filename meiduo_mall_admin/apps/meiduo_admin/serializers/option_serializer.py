from rest_framework import serializers

from goods.models import SpecificationOption, SPUSpecification


class SpecOptSerializer(serializers.ModelSerializer):
    """规格选项表的序列化器"""
    spec = serializers.StringRelatedField(read_only=True)
    spec_id = serializers.IntegerField()

    class Meta:
        model = SpecificationOption
        fields = ['id', 'value', 'spec', 'spec_id']


class SPUSpecSimpleSerializer(serializers.ModelSerializer):
    """SPU规格表的简单序列化器"""
    class Meta:
        model = SPUSpecification
        fields = ['id', 'name']
