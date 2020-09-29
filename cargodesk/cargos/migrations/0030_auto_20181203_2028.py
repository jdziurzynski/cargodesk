# Generated by Django 2.1 on 2018-12-03 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargos', '0029_auto_20181203_2016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='date',
            new_name='create_date',
        ),
        migrations.AddField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('active', 'active'), ('closed', 'closed')], default='active', max_length=10),
        ),
    ]
