# Generated by Django 2.2.12 on 2020-06-21 16:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('last_edited', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
