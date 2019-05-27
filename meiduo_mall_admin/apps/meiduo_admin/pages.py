
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class MyPage(PageNumberPagination):
    page_query_param = "page"
    page_size = 5
    page_size_query_param = "pagesize"
    max_page_size = 10


    def get_paginated_response(self, data):
        # 组织分页器的返回结果
        # data: 数据集 分页后的  子集
        return Response({
            "counts": self.page.paginator.count, # 用户总量
            "lists": data, # 分页数据子集
            "page": self.page.number, # 当前第几页
            "pages": self.page.paginator.num_pages, # 总页数
            "pagesize": self.page_size # 后端默认使用分页长度
        })