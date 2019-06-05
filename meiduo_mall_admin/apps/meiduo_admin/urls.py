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
from rest_framework.routers import SimpleRouter
from rest_framework_jwt.views import obtain_jwt_token

from meiduo_admin.views.admin_views import AdminView, GroupSimpleView
from meiduo_admin.views.brand_views import BrandView
from meiduo_admin.views.channel_views import GoodsChannelView
from meiduo_admin.views.data_views import *
from meiduo_admin.views.group_views import GroupView, PermissionSimpleView
from meiduo_admin.views.image_views import SKUImageView, SKUSimpleView
from meiduo_admin.views.option_views import SpecOptView, SPUSpecSimpleView
from meiduo_admin.views.order_views import OrderInfoView
from meiduo_admin.views.permission_views import PermissionView, ContentTypeView
from meiduo_admin.views.specs_views import SPUSpecView
from meiduo_admin.views.spu_views import SPUView, BrandSimpleView, SPUCategoryView
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
    url(r'^skus/$', SKUView.as_view({"get": "list", "post": "create"})),
    # 删除一个sku对象
    # url(r'^skus/(?P<pk>\d+)/$', SKUView.as_view()),
    url(r'^skus/(?P<pk>\d+)/$', SKUView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    # 获得三级分类
    url(r'^skus/categories/$', GoodsCategoryView.as_view()),
    # 获得spu信息
    url(r'^goods/simple/$', SPUSimpleView.as_view()),
    # 获得spu规格信息
    url(r'^goods/(?P<pk>\d+)/specs/$', SpecsView.as_view()),
    # 获取,保存SPU表数据
    url(r'^goods/$', SPUView.as_view({'get': 'list', 'post': 'create'})),
    # 删除,获得,更新一个SPU
    url(r'^goods/(?P<pk>\d+)/$', SPUView.as_view({'delete': 'destroy', 'get': 'retrieve', 'put': 'update'})),
    # 获取品牌信息
    url(r'^goods/brands/simple/$', BrandSimpleView.as_view()),
    # 获取一级分类消息
    url(r'^goods/channel/categories/$', SPUCategoryView.as_view()),
    # 获取二级和三级分类消息
    url(r'^goods/channel/categories/(?P<pk>\d+)/$', SPUCategoryView.as_view()),
    # 获取,新增SPU规格信息
    url(r'^goods/specs/$', SPUSpecView.as_view({'get': 'list', 'post': 'create'})),
    # 删除,获取,更新一个SPU规格信息
    url(r'^goods/specs/(?P<pk>\d+)/$', SPUSpecView.as_view({'delete': 'destroy', 'get': 'retrieve', 'put': 'update'})),
    # 获取,新增规格选项信息
    url(r'^specs/options/$', SpecOptView.as_view({'get': 'list', 'post': 'create'})),
    # 获取,删除,修改一个规格选项信息
    url(r'^specs/options/(?P<pk>\d+)/$',
        SpecOptView.as_view({'delete': 'destroy', 'get': 'retrieve', 'put': 'update'})),
    # 获取SPU规格的简单信息
    url(r'^goods/specs/simple/$', SPUSpecSimpleView.as_view()),
    # 获取,创建频道信息
    url(r'^goods/channels/$', GoodsChannelView.as_view({'get': 'list', 'post': 'create'})),
    # 删除,获取,更新一个频道信息
    url(r'^goods/channels/(?P<pk>\d+)/$',
        GoodsChannelView.as_view({'delete': 'destroy', 'get': 'retrieve', 'put': 'update'})),
    # 获取频道组信息
    url(r'^goods/channel_types/$', GoodsChannelView.as_view({'get': 'get_goodschannelgroup'})),
    # 获取一级分类信息
    url(r'^goods/categories/$', GoodsChannelView.as_view({'get': 'get_goodscategory'})),
    # 获取,新建商品品牌信息
    url(r'^goods/brands/$', BrandView.as_view({'get': 'list', 'post': 'create'})),
    # 删除,获取,更新一个商品品牌信息
    url(r'^goods/brands/(?P<pk>\d+)/$', BrandView.as_view({'delete': 'destroy', 'get': 'retrieve', 'put': 'update'})),
    # # 获取,新建图片信息
    url(r'^skus/images/$', SKUImageView.as_view({'get': 'list', 'post': 'create'})),
    # # 删除,获取,更新一个图片信息
    url(r'^skus/images/(?P<pk>\d+)/$', SKUImageView.as_view({'delete': 'destroy', 'get': 'retrieve', 'put': 'update'})),
    # 获取简单的sku信息
    url(r'^skus/simple/$', SKUSimpleView.as_view()),
    # 获取订单信息
    url(r'^orders/$', OrderInfoView.as_view({'get': 'list'})),
    # 获取订单详细信息
    url(r'^orders/(?P<pk>\d+)/$', OrderInfoView.as_view({'get': 'retrieve'})),
    # 修改订单表状态
    url(r'^orders/(?P<pk>\d+)/status/$', OrderInfoView.as_view({'put': 'partial_update'})),
    # 获取,保存权限数据
    url(r'^permission/perms/$', PermissionView.as_view({'get': 'list', 'post': 'create'})),
    # 获取权限类型
    url(r'^permission/content_types/$', ContentTypeView.as_view()),
    # 获取,修改,删除一个权限数据
    url(r'^permission/perms/(?P<pk>\d+)/$',
        PermissionView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    # 获取,保存用户组数据
    url(r'^permission/groups/$', GroupView.as_view({'get': 'list', 'post': 'create'})),
    # 获取,更新,删除单个用户组数据
    url(r'^permission/groups/(?P<pk>\d+)/$',
        GroupView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    # 获取权限表的简单数据
    url(r'^permission/simple/$', PermissionSimpleView.as_view()),
    # 获取,增加管理员数据
    url(r'^permission/admins/$', AdminView.as_view({'get': 'list', 'post': 'create'})),
    # 获取,修改,删除一个管理员数据
    url(r'^permission/admins/(?P<pk>\d+)/$',
        AdminView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    # 获取用户分组简单的信息
    url(r'^permission/groups/simple/$', GroupSimpleView.as_view()),
]

router = SimpleRouter()
router.register('skus/images', SKUImageView, 'images')
urlpatterns += router.urls
