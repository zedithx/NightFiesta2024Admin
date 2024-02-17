from rest_framework import serializers

from .models import Player


class PointSerializers(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = ('id', 'name', 'score')
        
    def get_id(self, obj):
        return obj.id[-6:]


