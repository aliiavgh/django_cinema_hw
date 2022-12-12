from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from django.shortcuts import render

from applications.account.serializers import RegisterSerializer

User = get_user_model()


class APIVIew:
    pass


class RegisterApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

