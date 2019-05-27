from django.contrib.auth.backends import ModelBackend
from django.http import HttpRequest
import re
from users.models import User


class MeiduoModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):

        try:

            user = User.objects.get(username=username)
        except:
            # 如果未查到数据，则返回None，用于后续判断
            try:
                user = User.objects.get(mobile=username)
            except:
                return None

        # 如果此次身份认证是后台站点登陆
        # 值允许超级管理员登陆
        # 区分是后台站登陆的情况下才需要判断超级管理员

        if request == None: # request == None
            # 后台管理站点登陆
            if not user.is_staff:
                return None


        # 判断密码
        if user.check_password(password):
            return user
        else:
            return None

