# Generated by Django 5.1.3 on 2025-01-12 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ITV', '0002_alter_trabajador_apellidos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.PositiveBigIntegerField(choices=[(1, 'administrador'), (2, 'cliente'), (3, 'trabajador')], default=1),
        ),
    ]
