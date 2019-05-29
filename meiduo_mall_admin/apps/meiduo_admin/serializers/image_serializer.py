from django.conf import settings
from fdfs_client.client import Fdfs_client
from rest_framework import serializers

from goods.models import SKUImage, SKU


class SKUImageSerializer(serializers.ModelSerializer):
    """SKU图片表的序列化器"""

    class Meta:
        model = SKUImage
        fields = ['id', 'sku', 'image']

    # 重写create方法使图片能上传到FastDFS
    def create(self, validated_data):
        file = validated_data.pop('image')
        fdfs_conn = Fdfs_client(settings.FDFS_CONF_PATH)
        result = fdfs_conn.upload_by_buffer(file.read())
        if result['Status'] == 'Upload successed.':
            validated_data['image'] = result['Remote file_id']
            return super().create(validated_data)
        raise serializers.ValidationError('上传图片失败')

    # 重写update方法使图片能更新到FastDFS
    def update(self, instance, validated_data):
        file = validated_data['image']
        fdfs_conn = Fdfs_client(settings.FDFS_CONF_PATH)
        result = fdfs_conn.upload_by_buffer(file.read())
        if result['Status'] == 'Upload successed.':
            instance.image = result['Remote file_id']
            instance.sku = validated_data['sku']
            instance.save()
            return instance
        raise serializers.ValidationError('上传图片失败')


class SKUSimpleSerializer(serializers.ModelSerializer):
    """SKU表的简单序列化器"""

    class Meta:
        model = SKU
        fields = ['id', 'name']
