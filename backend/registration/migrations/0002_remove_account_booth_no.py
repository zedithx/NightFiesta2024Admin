# Generated by Django 4.2.8 on 2023-12-30 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("registration", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="account", name="booth_no",),
    ]
