# Generated by Django 2.0.13 on 2019-07-11 13:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
        migrations.AddField(
            model_name='post',
            name='end_time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='終了時間'),
        ),
        migrations.AddField(
            model_name='post',
            name='show_flag',
            field=models.CharField(default=1, max_length=50, verbose_name='表示フラグ'),
        ),
        migrations.AddField(
            model_name='post',
            name='start_time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='開始時間'),
        ),
    ]
