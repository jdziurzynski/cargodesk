# Generated by Django 2.1.2 on 2018-10-19 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargos', '0004_auto_20181015_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='info',
            field=models.TextField(default='', max_length=100, null=True),
        ),
    ]