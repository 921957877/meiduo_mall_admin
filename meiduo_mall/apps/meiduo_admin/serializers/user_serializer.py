

from rest_framework import serializers
from users.models import User

from django.contrib.auth.hashers import make_password


# 定义一个用户的序列化器

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "mobile",
            "email",
            "password"
        ]

        extra_kwargs = {
            "password": {"write_only": True},
            "id": {"read_only": True},

            "username": {
                "min_length": 5,
                "max_length": 20
            }
        }


    # def validate_password(self, value):
    #     # 加密
    #     pass


    # def validate(self, attrs):
    #     password = attrs['password']
    #     # 加密
    #     return attrs


    def create(self, validated_data):
        # 创建用户的过程中，对密码进行加密处理

        # 提取前端传来的密码 -- 明文

        # 方案一： 先创建用户，在设置密文密码
        # password = validated_data.pop('password')
        # instance = self.Meta.model.objects.create(**validated_data) # 没有密码的
        # instance.set_password(password) # 密文密码,需要保存数据 save()
        # instance.save()


        # 方案二
        # instance = User.objects.create_user(**validated_data)

        # 方案三
        password = validated_data['password']
        # make_password直接将有效数据中的明文改为密文密码
        validated_data['password'] = make_password(password) # 加密
        instance = self.Meta.model.objects.create(**validated_data)


        return instance





