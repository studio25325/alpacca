# Generated by Django 2.0.13 on 2019-10-10 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chance', '0006_auto_20191009_1548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cgame',
            name='author',
        ),
    ]