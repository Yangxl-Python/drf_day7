from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from api.serializers import UserModelSerializer
from api.authentication import JWTAuthentication
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
