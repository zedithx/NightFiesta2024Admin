# Generated by Django 4.2.8 on 2023-12-21 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Player",
            fields=[
                (
                    "id",
                    models.CharField(
                        blank=True, db_column="rfid", primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(blank=True, db_column="name", null=True)),
                ("score", models.IntegerField(default=0, null=True)),
                ("time_in", models.DateTimeField(auto_now_add=True, null=True)),
                ("time_out", models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
