# Generated by Django 5.1.3 on 2025-01-13 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ITV', '0007_cliente_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajador',
            name='email',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='trabajador',
            name='nombre',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
