from django.contrib.auth.models import User
from django.db import models


# Create your models here.

# static roles

class Role(models.Model):
    ROLE_OPTIONS = (
        ('Admin', 'Admin'),
        ('Game Master', 'Game Master')
    )
    role = models.CharField(db_column="Role", choices=ROLE_OPTIONS, max_length=50)

    def __str__(self):
        return self.role


class Account(User):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, related_name='account', null=True)
    REQUIRED_FIELDS = ['username', 'role']
