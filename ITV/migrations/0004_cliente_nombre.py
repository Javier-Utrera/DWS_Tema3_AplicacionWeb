# Generated by Django 5.1.3 on 2025-01-10 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ITV', '0003_alter_cliente_codigo_postal_alter_cliente_dni_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
