# Generated by Django 2.0.3 on 2018-03-27 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_score_sum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='classname',
            field=models.ForeignKey(on_delete=False, related_name='class_score', to='base.ClassProfile'),
        ),
    ]