# Generated by Django 5.1.4 on 2024-12-11 14:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ITV', '0003_alter_factura_fecha_emision_factura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='fecha_emision_factura',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
