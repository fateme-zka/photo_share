# Generated by Django 4.0.5 on 2022-06-10 22:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_rename_image_photo_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 10, 22, 2, 59, 707515, tzinfo=utc)),
        ),
    ]
