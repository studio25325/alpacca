# Generated by Django 2.0.13 on 2019-10-09 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chance', '0004_auto_20191009_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cgame',
            name='games',
            field=models.IntegerField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='cgame',
            name='receive',
            field=models.IntegerField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='cgame',
            name='receive_error',
            field=models.IntegerField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='cgame',
            name='service',
            field=models.IntegerField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='cgame',
            name='service_error',
            field=models.IntegerField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='cgame',
            name='stroke',
            field=models.IntegerField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='cgame',
            name='stroke_error',
            field=models.IntegerField(default=0, max_length=100),
        ),
    ]
