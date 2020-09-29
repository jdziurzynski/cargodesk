# Generated by Django 2.1.2 on 2018-10-23 20:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargos', '0016_shipment_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shipment',
            old_name='date',
            new_name='load_date_from',
        ),
        migrations.AddField(
            model_name='shipment',
            name='load_date_to',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='shipment',
            name='unload_date_from',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='shipment',
            name='unload_date_to',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]