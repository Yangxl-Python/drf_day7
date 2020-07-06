import re

from rest_framework import serializers
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from api.models import User

re_email = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$'
re_phone = r'1[3-9][0-9]{9}'


class UserModelSerializer(serializers.ModelSerializer):
    account = serializers.CharField(write_only=True)
    pwd = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('account', 'pwd', 'username', 'email', 'phone')
        extra_kwargs = {
            'username': {
                'read_only': True
            },
            'email': {
                'read_only': True
            },
            'phone': {
                'read_only': True
            }
        }

    def validate(self, attrs):
        account = attrs.get('account')
        pwd = attrs.get('pwd')

        if re.match(re_email, account):
            user = User.objects.filter(email=account).first()
        elif re.match(re_phone, account):
            user = User.objects.filter(phone=account).first()
        else:
            user = User.objects.filter(username=account).first()

        if user and user.check_password(pwd):
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            self.token = token
            self.obj = user
        else:
            raise serializers.ValidationError('用户名或密码错误')

        return attrs
