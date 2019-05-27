"""meiduo_mall_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from meiduo_admin.views.data_views import *
from meiduo_admin.views.user_views import *
from meiduo_admin.views.sku_views import *


urlpatterns = [
    url(r'^authorizations/', obtain_jwt_token),

    # 获得用户总数
    url(r'^statistical/total_count/', UserTotalCountView.as_view()),
    # 获得当日新增用户
    url(r'^statistical/day_increment/', UserDayIncrView.as_view()),
    # 日活跃用户
    url(r'^statistical/day_active/', UserDayActivateView.as_view()),
    # 日下单用户量
    url(r'^statistical/day_orders/', UserDayOrdersView.as_view()),
    # 最近30天每一天的用户增量
    url(r'^statistical/month_increment/', UserMonthIncrView.as_view()),
    # 返回商品类别访问量
    url(r'^statistical/goods_day_views/', GoodsVisitView.as_view()),


    # 获得用户数据，新建用户
    url(r'^users/$', UserView.as_view()),


    # 获得sku商品数据
    # url(r'^skus/$', SKUView.as_view()),
    url(r'^skus/$', SKUView.as_view({"get":"list", "post":"create"})),
    # 删除一个sku对象
    # url(r'^skus/(?P<pk>\d+)/$', SKUView.as_view()),
    url(r'^skus/(?P<pk>\d+)/$', SKUView.as_view({"get":"retrieve", "put":"update", "delete":"destroy"})),

    # 获得三级分类
    url(r'^skus/categories/$', GoodsCategoryView.as_view()),

    # 获得spu信息
    url(r'^goods/simple/$', SPUSimpleView.as_view()),
    # 获得spu规格信息
    url(r'^goods/(?P<pk>\d+)/specs/$', SpecsView.as_view()),

]
