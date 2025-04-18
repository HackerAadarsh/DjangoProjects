# Generated by Django 5.1.7 on 2025-04-10 02:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("player", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="song",
            name="album",
            field=models.ForeignKey(
                default=2,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="songs",
                to="player.album",
            ),
            preserve_default=False,
        ),
    ]
