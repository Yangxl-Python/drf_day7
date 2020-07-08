from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from api import views

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('detail/', views.UserDetailAPIView.as_view()),
    path('user_login/', views.UserLoginAPIView.as_view()),
    path('computers/', views.ComputerListAPIView.as_view())
]
