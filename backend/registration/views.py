import os
import bcrypt
import os

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
from .permissions import IsStaff
from . import serializers
from .models import Account, Role
from booths.models import Player


class AccountView(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated, IsStaff]

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

    @action(detail=False, methods=['post'], url_path=r'login_account', permission_classes=[])
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
                    'is_staff': user.is_staff,
                    'name': username
                })
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response(e.args, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['get'], url_path=r'logout_account')
    def logout_account(self, request, *args, **kwargs):
        try:
            logout(request)
            return Response({f"{request.user} has logged out successfully."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e.args, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=["post"], url_path=r"register_player")
    def register_player(self, request, *args, **kwargs):
        try:
            data = self.request.data
            rfid = data.get('rfid')
            name = data.get('name')
            if data.get('education'):
                education = data.get('education')
            occupation = data.get('occupation')
            player = Player(id=rfid, name=name, occupation=occupation)
            if education:
                player.education = education
            player.save()
            return Response({'detail': f'Player {name} with rfid number {rfid[:8]} has been created.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e.args, status=status.HTTP_404_NOT_FOUND)
