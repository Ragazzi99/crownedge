# Generated by Django 4.0.3 on 2022-05-11 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_booking_booking_date_booking_del_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='checkout_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='future',
            field=models.BooleanField(default=False),
        ),
    ]
