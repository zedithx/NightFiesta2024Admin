from django.contrib.auth.models import User
from django.db import models


class Records(models.Model):
    player = models.ForeignKey(to='Player', on_delete=models.SET_NULL, related_name='player', blank=True, null=True)
    score_added = models.IntegerField(db_column="score added", blank=True)
    time = models.DateTimeField(auto_now_add=True, null=True)
    game_master = models.CharField(db_column="game master", null=True, blank=True)


class Player(models.Model):
    ORGANIZATION_OPTIONS = (
        ('SUTD', 'SUTD'),
        ('Public', 'Public')
    )
    id = models.CharField(db_column='rfid', primary_key=True, blank=True)
    name = models.CharField(db_column='name', blank=True, null=True)
    score = models.IntegerField(default=0, null=True)
    organization = models.CharField(db_column='organization', choices=ORGANIZATION_OPTIONS, max_length=50)
    time_in = models.DateTimeField(auto_now_add=True, null=True)
    time_out = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name



