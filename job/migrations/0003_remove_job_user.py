# Generated by Django 3.0.6 on 2020-05-12 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_auto_20200511_2146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='user',
        ),
    ]
