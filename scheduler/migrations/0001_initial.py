# Generated by Django 2.2 on 2019-07-05 02:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=50, verbose_name='概要')),
                ('description', models.TextField(blank=True, verbose_name='詳細な説明')),
                ('show_flag', models.CharField(default=1, max_length=50, verbose_name='表示フラグ')),
                ('start_time', models.TimeField(default=datetime.time(7, 0), verbose_name='開始時間')),
                ('end_time', models.TimeField(default=datetime.time(7, 0), verbose_name='終了時間')),
                ('date', models.DateField(verbose_name='日付')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2019, 7, 5, 2, 20, 52, 963522, tzinfo=utc), verbose_name='作成日')),
            ],
        ),
    ]
