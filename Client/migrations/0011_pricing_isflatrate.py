# Generated by Django 4.1.7 on 2023-04-20 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0010_alter_notifications_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricing',
            name='isflatrate',
            field=models.BooleanField(default=False),
        ),
    ]
