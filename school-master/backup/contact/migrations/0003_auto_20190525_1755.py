# Generated by Django 2.2.1 on 2019-05-25 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='location',
            name='log',
        ),
    ]
