from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class MyPageNumberPagination(PageNumberPagination):
    page_size = 3
    max_page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'page'


class MyLimitPagination(LimitOffsetPagination):
    default_limit = 3
    limit_query_param = "limit"
    offset_query_param = "offset"
    max_limit = 5
