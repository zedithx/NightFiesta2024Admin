from django.db import models
from registration.models import Account


class Player(models.Model):
    id = models.CharField(db_column='rfid', primary_key=True, blank=True)
    name = models.CharField(db_column='name', blank=True, null=True)
    score = models.IntegerField(default=0, null=True)
    time_in = models.DateTimeField(auto_now_add=True, null=True)
    time_out = models.DateTimeField(auto_now=True, null=True)
    last_updated_by = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name='player', null=True)
