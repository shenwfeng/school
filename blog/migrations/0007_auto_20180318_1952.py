# Generated by Django 2.0.3 on 2018-03-18 11:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180318_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticles',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 18, 11, 52, 26, 877725, tzinfo=utc)),
        ),
    ]
