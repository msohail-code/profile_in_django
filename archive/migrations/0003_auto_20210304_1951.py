# Generated by Django 2.1.15 on 2021-03-05 01:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0002_auto_20210225_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 5, 1, 51, 25, 546089, tzinfo=utc)),
        ),
    ]
