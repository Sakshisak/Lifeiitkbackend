# Generated by Django 2.2.2 on 2019-06-24 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventmodel',
            name='acad_state',
        ),
        migrations.RemoveField(
            model_name='eventmodel',
            name='acads',
        ),
    ]