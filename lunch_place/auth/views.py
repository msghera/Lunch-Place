from .serializers import TokenObtainPairSerializer, RegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.models import User
from rest_framework import generics


class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = TokenObtainPairSerializer


class EmployeeRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
