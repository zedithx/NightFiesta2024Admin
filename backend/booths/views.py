# Create your views here.
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from . import serializers
from .models import Player


class BoothsView(viewsets.GenericViewSet):

    @action(detail=False, methods=["post"], url_path=r"add-points")
    def add_points(self, request, *args, **kwargs):
        try:
            data = self.request.data
            print(data)
            rfid = str(data.get('rfid'))
            points = int(data.get('points'))
            # retrieve player in db
            player = Player.objects.get(id=rfid)
            # add points
            player.score += points
            player.save()
            # return serialized data of id and score
            result = serializers.PointSerializers(player).data
            return Response(result, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(e.args, status=status.HTTP_404_NOT_FOUND)
