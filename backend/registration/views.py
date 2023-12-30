import os

from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
import bcrypt
import os

from . import serializers
from .models import Account, Role



class AccountView(viewsets.GenericViewSet):
    @action(detail=False, methods=['post'], url_path=r'create_account')
    def create_account(self, request, *args, **kwargs):
        try:
            data = request.data
            # attain parameters posted to be stored
            username = data.get('username')
            hashed = bcrypt.hashpw(data.get('password').encode('utf8'), b'$2b$12$RODwzTBjKDreOge5RtwNDe')
            role = Role.objects.get(role=data.get('role'))

            account = Account(
                username=username,
                password=hashed,
                role=role
            )

            account.password = make_password(hashed)
            account.is_active = True
            account.save()
            return Response({'detail': f'Account {username} has been created.'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(e.args, status=status.HTTP_404_NOT_FOUND)

# Create your views here.