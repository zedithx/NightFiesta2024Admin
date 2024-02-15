# Generated by Django 4.2.8 on 2024-02-13 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booths", "0002_remove_player_records_records_player"),
    ]

    operations = [
        migrations.RemoveField(model_name="player", name="organization",),
        migrations.AddField(
            model_name="player",
            name="education",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Secondary", "Secondary"),
                    ("Post-Secondary", "Post-Secondary"),
                    ("University", "University"),
                    ("Others", "Others"),
                ],
                db_column="education",
                max_length=50,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="player",
            name="occupation",
            field=models.CharField(
                choices=[
                    ("SUTD Student", "SUTD Student"),
                    ("SUTD Staff", "SUTD Staff"),
                    ("Outside Student", "Outside Student"),
                    ("NS", "NS"),
                    ("Others", "Others"),
                ],
                db_column="occupation",
                default="SUTD Student",
                max_length=50,
            ),
            preserve_default=False,
        ),
    ]
