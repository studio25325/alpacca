# Generated by Django 2.0.13 on 2019-10-09 06:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cgame',
            name='receive',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='cmatch',
            name='author',
            field=models.ForeignKey(default='alpacca', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]