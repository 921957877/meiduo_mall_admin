


from rest_framework.response import Response
from rest_framework.generics import ListAPIView,CreateAPIView
from users.models import User
from meiduo_admin.serializers.user_serializer import *

from meiduo_admin.pages import MyPage


# /meiduo_admin/users/?keyword=<搜索内容>&page=<页码>&pagesize=<页容量>
class UserView(ListAPIView, CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = MyPage

    def get_queryset(self):
        # 获得数据集
        # 尝试获得keyword
        keyword = self.request.query_params.get("keyword")

        # 判断过滤的keyword存不存在（前端传没传）
        if keyword:
            return self.queryset.filter(username__contains=keyword)

        return self.queryset.all()


