from rest_framework import serializers

from goods.models import SPUSpecification


class SPUSpecSerializer(serializers.ModelSerializer):
    """SPU规格表的序列化器"""
    spu = serializers.StringRelatedField(read_only=True)
    spu_id = serializers.IntegerField()

    class Meta:
        model = SPUSpecification
        fields = ['id', 'name', 'spu', 'spu_id']
