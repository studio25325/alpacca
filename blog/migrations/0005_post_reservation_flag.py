# Generated by Django 2.0.13 on 2019-07-18 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190711_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='reservation_flag',
            field=models.CharField(default=1, max_length=50, verbose_name='予約フラグ'),
        ),
    ]