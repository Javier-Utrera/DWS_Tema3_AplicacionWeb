# Generated by Django 5.1.3 on 2025-01-13 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ITV', '0004_alter_maquinaria_tipo_alter_trabajador_puesto_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='dni',
            field=models.CharField(max_length=9, null=True, unique=True),
        ),
    ]
