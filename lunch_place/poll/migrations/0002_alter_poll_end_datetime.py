# Generated by Django 4.0.4 on 2022-05-01 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='end_datetime',
            field=models.DateTimeField(null=True),
        ),
    ]
