# Generated by Django 5.1.6 on 2025-02-13 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0002_booking_dropoff_location_booking_pickup_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='payment_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Successful', 'Successful'), ('Failed', 'Failed')], default='Pending', max_length=20),
        ),
    ]
