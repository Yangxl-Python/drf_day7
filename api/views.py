from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from api.models import Computer
from api.pagination import MyPageNumberPagination, MyLimitPagination
from api.serializers import UserModelSerializer, ComputerModelSerializer
from api.authentication import JWTAuthentication
from api.filter import LimitFilter, ComputerFilterSet
from utils.response import APIResponse


class UserDetailAPIView(APIView):
    # authentication_classes = [JSONWebTokenAuthentication]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return APIResponse(results={"username": request.user.username})


class UserLoginAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        ser = UserModelSerializer(data=request.data)
        ser.is_valid(raise_exception=True)

        return APIResponse(token=ser.token, results=UserModelSerializer(ser.obj).data)


class ComputerListAPIView(ListAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerModelSerializer
    filter_backends = [SearchFilter, OrderingFilter, LimitFilter, DjangoFilterBackend]
    search_fields = ["name", "price"]
    ordering = ["price"]

    # pagination_class = MyPageNumberPagination
    pagination_class = MyLimitPagination

    filter_class = ComputerFilterSet
