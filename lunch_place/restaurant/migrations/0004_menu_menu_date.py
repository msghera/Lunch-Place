# Generated by Django 4.0.4 on 2022-04-29 18:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_restaurant_options_alter_restaurant_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='menu_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
