# Generated by Django 2.1.15 on 2021-03-18 17:13

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0014_auto_20210318_2159'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_images',
            new_name='Images',
        ),
        migrations.AlterField(
            model_name='userfile',
            name='uploadDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 18, 17, 13, 7, 830868, tzinfo=utc)),
        ),
    ]
