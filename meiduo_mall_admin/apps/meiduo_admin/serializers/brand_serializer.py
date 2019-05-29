from django.conf import settings
from fdfs_client.client import Fdfs_client
from rest_framework import serializers

from goods.models import Brand


class BrandSerializer(serializers.ModelSerializer):
    """商品品牌表的序列化器"""

    class Meta:
        model = Brand
        fields = ['id', 'name', 'logo', 'first_letter']

    # 重写create方法使图片能够保存到FastDFS中
    def create(self, validated_data):
        # 获取图片对象,构建成一个文件对象
        file = validated_data.pop('logo')
        # 创建FastDFS连接对象
        fdfs_conn = Fdfs_client(settings.FDFS_CONF_PATH)
        # 上传图片到FastDFS
        result = fdfs_conn.upload_by_buffer(file.read())
        # 判断是否上传成功
        if result['Status'] == 'Upload successed.':
            # 获取上传成功后的路径
            image_url = result['Remote file_id']
            validated_data['logo'] = image_url
            return super().create(validated_data)
        raise serializers.ValidationError('上传图片失败')

    # 重写update方法使图片能更新到FastDFS中
    def update(self, instance, validated_data):
        # 获取图片对象,构建成一个文件对象
        file = validated_data.pop('logo')
        # 创建FastDFS连接对象
        fdfs_conn = Fdfs_client(settings.FDFS_CONF_PATH)
        # 上传图片到FastDFS
        result = fdfs_conn.upload_by_buffer(file.read())
        # 判断是否上传成功
        if result['Status'] == 'Upload successed.':
            image_url = result['Remote file_id']
            instance.logo = image_url
            instance.name = validated_data['name']
            instance.first_letter = validated_data['first_letter']
            instance.save()
            return instance
        raise serializers.ValidationError('上传图片失败')
