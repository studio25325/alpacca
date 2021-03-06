# Generated by Django 2.0.13 on 2019-10-09 01:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_id', models.CharField(default=1, max_length=200)),
                ('stroke', models.CharField(default=0, max_length=100)),
                ('stroke_error', models.CharField(default=0, max_length=100)),
                ('service', models.CharField(default=0, max_length=100)),
                ('service_error', models.CharField(default=0, max_length=100)),
                ('net', models.CharField(default=0, max_length=100)),
                ('net_error', models.CharField(default=0, max_length=100)),
                ('games', models.CharField(default=0, max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.CharField(default='大凱', max_length=100)),
                ('opponent', models.CharField(default='対戦相手', max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
