

from rest_framework.views import APIView
from datetime import date,datetime
from users.models import User
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

# 获得用户总数
# GET
# token
# 返回数据： count，date

class UserTotalCountView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        # 获得当前的查询日期
        cur_date = date.today() # 2019-5-24

        # 获得用户总数
        count = User.objects.count()

        # 构建数据返回
        return Response({
            "count": count,
            "date": cur_date
        })


# 获得当前新增用户数量
# GET
# 参数无
# 返回count，date

# pip3 install pytz
import pytz
from django.conf import settings

class UserDayIncrView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request):
        # 获得当前日期
        cur_date = date.today() # 2019-5-26

        # 2019-5-26 0:0:0  Asia/Shanghai
        cur_date = datetime(year=cur_date.year, month=cur_date.month, day=cur_date.day,
                            hour=0, minute=0, second=0,
                            tzinfo=pytz.timezone(settings.TIME_ZONE))

        # 过滤出当前日期新创建的用户
        # 创建日期大于等于 2019-5-26 0:0:0
        count = User.objects.filter(date_joined__gte=cur_date).count()
        # 返回数据
        return Response({
            "count": count,
            "date": cur_date
            # "date": cur_date.date()
        })


# GET
# 路径
# 返回值

class UserDayActivateView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request):
        # 获得当前日期
        cur_date = date.today()
        cur_date = datetime(year=cur_date.year, month=cur_date.month, day=cur_date.day,
                            hour=0, minute=0, second=0,
                            tzinfo=pytz.timezone(settings.TIME_ZONE))
        # 过滤出最后登陆的日期是当天
        query =  User.objects.filter(last_login__gte=cur_date)
        count = query.count()
        # 返回
        return Response({
            "count": count,
            "date": cur_date
        })


from orders.models import OrderInfo
class UserDayOrdersView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request):
        # 获得当天日期
        cur_date = date.today()
        cur_date = datetime(year=cur_date.year, month=cur_date.month, day=cur_date.day,
                            hour=0, minute=0, second=0,
                            tzinfo=pytz.timezone(settings.TIME_ZONE))

        # 根据已知条件查询目标数据
        # 已知条件是从表条件还是主表条件
        # 1、从从表入手； 2、从主表入手查询


        # 从从表入手查询： 分2部
        # 第一步：找从表对象
        # 第二步：在从表对象中找主表对象
        # # 根据日期，过滤出所有订单
        # order_query = OrderInfo.objects.filter(create_time__gte=cur_date)
        # user_list = []
        # for order in order_query:
        #     # order 是一个 订单对象
        #     user_list.append(order.user)
        #
        # # 在所有订单中找出用户，统计用户数据, 去重
        # count = len(set(user_list))


        # 从主表入手
        # 已知条件：订单创建日期（从表）
        # 查询目标数据： 用户
        # 从表小写_set: 主表中默认关联从表的所有数据对象； 在从表中的外键字段添加约束related_name指明关联字段
        # 注意：获得的主表数据集需要经过去重
        user_queryset = set(User.objects.filter(orders__create_time__gte=cur_date))
        count = len(user_queryset)

        # 返回
        return Response({
            "count": count,
            "date": cur_date
        })







# 统计最近30天，每一天新增用户量
# GET
# 参数token
# 返回数据
from datetime import timedelta
class UserMonthIncrView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request):
        # 获得当天日期
        cur_date = date.today()
        cur_date = datetime(year=cur_date.year, month=cur_date.month, day=cur_date.day,
                            hour=0, minute=0, second=0,
                            tzinfo=pytz.timezone(settings.TIME_ZONE))
        # 获得起始日期
        # 5-24  减去  29天
        # timedelta对象是一个时间段，days=29代表29天
        # cur_date是一个时间点对象
        start_date = cur_date - timedelta(days=29)

        user_list = []
        # 遍历这30天，统计每一天用户增量
        for index in range(30): # 0,1,2,3,4,5....29
            # calc_date就是用于计算用户增量的那一天！
            calc_date = start_date + timedelta(days=index)

            # calc_date:  4-25
            # 4-25 0：0：0    <=  User.create_time   <  4-26 0:0:0
            count = User.objects.filter(date_joined__gte=calc_date,
                                date_joined__lt=calc_date+timedelta(days=1)
                                ).count()

            data = {
                "count": count,
                "date": calc_date
            }

            user_list.append(data)


        # 构建数据返回
        return Response(user_list)





from rest_framework import serializers
from goods.models import GoodsVisitCount
from rest_framework.generics import ListAPIView

class GoodsVisitCountSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = GoodsVisitCount
        fields = ["count", "category"]


class GoodsVisitView(ListAPIView):
    permission_classes = [IsAdminUser]
    # queryset = GoodsVisitCount.objects.filter(date=date.today())
    queryset = GoodsVisitCount.objects.all()
    serializer_class = GoodsVisitCountSerializer


    def get_queryset(self):
        return self.queryset.filter(date=date.today())









