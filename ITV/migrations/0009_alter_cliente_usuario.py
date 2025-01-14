# Generated by Django 5.1.3 on 2025-01-14 08:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ITV', '0008_trabajador_email_trabajador_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_Cliente', to=settings.AUTH_USER_MODEL),
        ),
    ]
