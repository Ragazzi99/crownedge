# Generated by Django 4.0.3 on 2022-05-13 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_alter_booking_future'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='display',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='future',
            field=models.BooleanField(default=False),
        ),
    ]
