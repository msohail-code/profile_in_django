# Generated by Django 2.1.15 on 2021-03-18 17:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0017_auto_20210318_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 18, 17, 13, 7, 838864, tzinfo=utc)),
        ),
    ]
