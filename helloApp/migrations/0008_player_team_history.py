# Generated by Django 5.1.3 on 2025-02-22 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloApp', '0007_player_profile_image_alter_player_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='team_history',
            field=models.TextField(default='所属チームなし'),
        ),
    ]
