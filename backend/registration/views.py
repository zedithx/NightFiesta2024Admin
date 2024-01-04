import os

from django.contrib.auth import authenticate, login
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password
import bcrypt
import os

from rest_framework_simplejwt.tokens import RefreshToken

from . import serializers
from .models import Account, Role
from booths.models import Player


class AccountView(viewsets.GenericViewSet):
    @action(detail=False, methods=['post'], url_path=r'create_account')
    def create_account(self, request, *args, **kwargs):
        try:
            data = self.request.data
            # attain parameters posted to be stored
            username = data.get('username')
            password = data.get('password')
            hashed = bcrypt.hashpw(password.encode(), os.environ.get('SALT_KEY').encode())
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

    @action(detail=False, methods=['post'], url_path=r'login_account')
    def login_account(self, request, *args, **kwargs):
        try:
            data = self.request.data
            username = data.get('username')
            password = data.get('password')
            hashed = bcrypt.hashpw(password.encode(), os.environ.get("SALT_KEY").encode())
            user = authenticate(username=username, password=hashed)
            if user is not None:
                refresh = RefreshToken.for_user(user)
                access_token = refresh.access_token

                return Response({
                    'access': str(access_token),
                    'refresh': str(refresh),
                })
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response(e.args, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=["post"], url_path=r"register_player")
    @permission_classes([IsAuthenticated])
    def register_player(self, request, *args, **kwargs):
        try:
            data = self.request.data
            rfid = data.get('rfid')
            name = data.get('name')
            teletag = data.get('teletag')
            player = Player(id=rfid, name=name, teletag=teletag)
            player.last_updated_by = self.request.user
            player.save()
            return Response({'detail': f'Player {name} has been created by {request.user}.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e.args, status=status.HTTP_404_NOT_FOUND)