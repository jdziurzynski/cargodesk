# Generated by Django 2.0.9 on 2018-12-06 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cargos', '0033_auto_20181206_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]