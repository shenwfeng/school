# Generated by Django 2.0.3 on 2018-03-19 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20180319_0951'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='once_in_class',
            field=models.ManyToManyField(related_name='onceinclass', to='base.ClassProfile'),
        ),
        migrations.AlterField(
            model_name='student',
            name='now_in_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nowinclass', to='base.ClassProfile'),
        ),
    ]
