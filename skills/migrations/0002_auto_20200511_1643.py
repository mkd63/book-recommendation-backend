# Generated by Django 2.2.2 on 2020-05-11 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='skill_level',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
