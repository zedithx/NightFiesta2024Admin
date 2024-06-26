# Generated by Django 4.2.8 on 2024-02-04 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Records",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "score_added",
                    models.IntegerField(blank=True, db_column="score added"),
                ),
                ("time", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "game_master",
                    models.CharField(blank=True, db_column="game master", null=True),
                ),
            ],
        ),
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
                (
                    "organization",
                    models.CharField(
                        choices=[("SUTD", "SUTD"), ("Public", "Public")],
                        db_column="organization",
                        max_length=50,
                    ),
                ),
                ("time_in", models.DateTimeField(auto_now_add=True, null=True)),
                ("time_out", models.DateTimeField(auto_now=True, null=True)),
                (
                    "records",
                    models.ManyToManyField(
                        blank=True, related_name="player_records", to="booths.records"
                    ),
                ),
            ],
        ),
    ]
