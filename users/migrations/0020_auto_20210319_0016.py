# Generated by Django 2.1.15 on 2021-03-18 19:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20210318_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='featured',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userfile',
            name='uploadDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 18, 19, 16, 2, 435120, tzinfo=utc)),
        ),
    ]