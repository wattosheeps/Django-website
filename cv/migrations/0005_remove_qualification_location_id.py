# Generated by Django 2.2.12 on 2020-06-23 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0004_qualification_location_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qualification',
            name='location_id',
        ),
    ]
