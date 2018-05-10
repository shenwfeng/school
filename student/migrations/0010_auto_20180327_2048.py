# Generated by Django 2.0.3 on 2018-03-27 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_auto_20180327_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='chinese',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='score',
            name='english',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='score',
            name='math',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='score',
            name='sum',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
    ]
