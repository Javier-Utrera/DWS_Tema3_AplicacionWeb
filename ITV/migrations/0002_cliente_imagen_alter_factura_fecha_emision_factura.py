# Generated by Django 5.1.4 on 2024-12-11 14:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ITV', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='imagen',
            field=models.ImageField(default='imagenes/icono.png', upload_to='imagenes/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='factura',
            name='fecha_emision_factura',
            field=models.DateField(default=datetime.datetime(2024, 12, 11, 14, 20, 19, 178644)),
        ),
    ]