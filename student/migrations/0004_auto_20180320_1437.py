# Generated by Django 2.0.3 on 2018-03-20 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20180319_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='starttime',
            field=models.DateField(null=True),
        ),
    ]
