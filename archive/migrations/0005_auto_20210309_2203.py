# Generated by Django 2.1.15 on 2021-03-10 04:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0004_auto_20210306_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 10, 4, 3, 14, 818437, tzinfo=utc)),
        ),
    ]