# Generated by Django 2.0.3 on 2018-03-18 02:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticles',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 18, 2, 10, 16, 250601, tzinfo=utc)),
        ),
    ]