# Generated by Django 2.1.2 on 2018-10-21 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargos', '0014_auto_20181021_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='currency',
            field=models.CharField(choices=[('euro', 'euro'), ('sek', 'sek'), ('pln', 'pln')], default='euro', max_length=10),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='truck_type',
            field=models.CharField(choices=[('Tautliner', 'Tautliner'), ('Frigo', 'Frigo'), ('Tank', 'Tank')], default='Tautliner', max_length=10),
        ),
    ]