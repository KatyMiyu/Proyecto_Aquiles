# Generated by Django 4.1.2 on 2024-07-08 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_nav_home_url_home'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nav_home',
            name='url_home',
            field=models.CharField(default='default_value', max_length=100),
        ),
    ]
