# Generated by Django 4.1.7 on 2023-04-18 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0007_notifications_timestamp'),
    ]

    operations = [

        migrations.AlterField(
            model_name='notifications',
            name='message',
            field=models.CharField(default='', max_length=100),
        ),
    ]