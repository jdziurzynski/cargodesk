# Generated by Django 2.1.2 on 2018-11-08 18:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargos', '0021_shipment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='closed_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
