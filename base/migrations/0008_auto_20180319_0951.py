# Generated by Django 2.0.3 on 2018-03-19 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20180318_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursename', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='schoolterm',
            unique_together={('term', 'schoolyearname')},
        ),
    ]
