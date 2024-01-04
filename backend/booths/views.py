# Create your views here.
from django.core.paginator import Paginator
from django.utils.functional import cached_property
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from . import serializers
from .models import Player


class FasterDjangoPaginator(Paginator):
    @cached_property
    def count(self):
        # only select 'rfid' for counting, much cheaper
        return self.object_list.values('id').count()


class StandardResultsSetPagination(PageNumberPagination):
    django_paginator_class = FasterDjangoPaginator
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 25


class BoothsView(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    @action(detail=False, methods=["post"], url_path=r"add_points")
    def add_points(self, request, *args, **kwargs):
        """Add points to player by their rfid after playing a game"""
        try:
            data = self.request.data
            rfid = str(data.get('rfid'))
            points = int(data.get('points'))
            # retrieve player in db
            player = Player.objects.get(id=rfid)
            # add points
            player.score += points
            # player.last_updated_by(self.request.user)
            # return serialized data of id and score
            result = serializers.PointSerializers(player).data
            player.last_updated_by = self.request.user
            player.save()
            return Response(result, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(e.args, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=["get"], url_path=r"leaderboard")
    def leaderboard(self, request, *args, **kwargs):
        """return name, score and ranking of all players, with pagination"""
        try:
            players = Player.objects.all()
            print(players)
            players = players.order_by('score')
            pages = self.paginate_queryset(players)
            serialized = serializers.PointSerializers(pages, many=True, partial=True).data
            return self.get_paginated_response(serialized)
        except Exception as e:
            return Response(e.args, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=["post"], url_path=r"points_name")
    def points_name(self, request, *args, **kwargs):
        """return points and name and rank after querying by name. To be used as search filter for leaderboard
        on webpage"""
        try:
            data = self.request.data
            player = Player.objects.get(name__icontains=data.get('name'))
            result = serializers.PointSerializers(player).data
            return Response(result, status.HTTP_200_OK)
        except Exception as e:
            return Response(e.args, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=["post"], url_path=r"points_rfid")
    def points_rfid(self, request, *args, **kwargs):
        """return points and name and rank after querying by rfid. To be used at the booths if someone wants to check
        their points"""
        try:
            data = self.request.data
            player = Player.objects.get(id=data.get('rfid'))
            result = serializers.PointSerializers(player).data
            return Response(result, status.HTTP_200_OK)
        except Exception as e:
            return Response(e.args, status=status.HTTP_404_NOT_FOUND)
