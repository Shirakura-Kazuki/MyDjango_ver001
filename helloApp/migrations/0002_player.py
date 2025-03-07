# Generated by Django 5.1.3 on 2025-02-21 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('category', models.CharField(choices=[('選手', '選手'), ('その他', 'その他')], max_length=10)),
                ('team', models.CharField(choices=[('giants', '読売ジャイアンツ'), ('tigers', '阪神タイガース'), ('dragons', '中日ドラゴンズ'), ('baystars', '横浜DeNAベイスターズ'), ('carp', '広島東洋カープ'), ('swallows', '東京ヤクルトスワローズ'), ('buffaloes', 'オリックス・バファローズ'), ('hawks', '福岡ソフトバンクホークス'), ('fighters', '北海道日本ハムファイターズ'), ('marines', '千葉ロッテマリーンズ'), ('lions', '埼玉西武ライオンズ'), ('eagles', '東北楽天ゴールデンイーグルス'), ('kintetsu', '大阪近鉄バファローズ'), ('others', 'その他')], max_length=100)),
                ('profile', models.TextField()),
            ],
        ),
    ]
