from rest_framework import serializers
from .models import Player


class PointSerializers(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('name', 'score')
