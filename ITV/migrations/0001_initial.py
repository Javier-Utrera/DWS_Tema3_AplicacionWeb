# Generated by Django 5.1.2 on 2024-10-28 12:19

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(blank=True, max_length=50)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1)),
                ('fecha_nacimiento', models.DateField()),
                ('codigo_postal', models.IntegerField()),
                ('domicilio', models.TextField()),
                ('correo', models.EmailField(max_length=50)),
                ('telefono', models.PositiveIntegerField()),
                ('dni', models.CharField(max_length=9, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmpresaExterna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('municipio', models.CharField(max_length=50)),
                ('coste', models.FloatField()),
                ('cif', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Inspeccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inspeccion', models.DateField(default=django.utils.timezone.now)),
                ('resultado_inspeccion', models.CharField(max_length=100)),
                ('notas_inspeccion', models.TextField()),
                ('cliente_puntual', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.FloatField()),
                ('metros', models.DecimalField(decimal_places=3, max_digits=50)),
                ('anio_arrendamiento', models.DateField()),
                ('duenio', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=7)),
                ('fecha_matriculacion', models.DateField(help_text='Este campo o el numero de bastidor debe estar relleno', null=True)),
                ('numero_bastidor', models.CharField(max_length=17)),
                ('tipo_inspeccion', models.CharField(choices=[('PE', 'Periodica'), ('NOPE', 'NoPeriodica'), ('VETAX', 'VerificacionTaximetro'), ('VETAXV', 'VerificacionTaximetroCambioVehiculo')], max_length=7)),
                ('remolque', models.BooleanField(default=False)),
                ('tipo_pago', models.CharField(choices=[('TA', 'Tarjeta'), ('EF', 'Efectivo')], max_length=2)),
                ('fecha_propuesta', models.DateField(null=True)),
                ('hora_propuesta', models.TimeField(null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente_Cita', to='ITV.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='EstacionItv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('munipio', models.CharField(max_length=50)),
                ('eficiencia_energetica', models.CharField(max_length=1)),
                ('comunidad_autonoma', models.CharField(max_length=20)),
                ('cliente', models.ManyToManyField(related_name='cliente_EstacionItv', through='ITV.Cita', to='ITV.cliente')),
                ('local', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='local_EstacionItv', to='ITV.local')),
            ],
        ),
        migrations.AddField(
            model_name='cita',
            name='estacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estacionitv_Cita', to='ITV.estacionitv'),
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('importe', models.DecimalField(decimal_places=2, max_digits=50)),
                ('pagado', models.BooleanField(default=False)),
                ('fecha_emision_factura', models.DateField(default=django.utils.timezone.now)),
                ('observaciones', models.TextField()),
                ('inspeccion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='inspeccion_Factura', to='ITV.inspeccion')),
            ],
        ),
        migrations.CreateModel(
            name='Maquinaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tipo', models.CharField(choices=[('EM', 'Emisiones'), ('FR', 'Frenos'), ('DI', 'Direccion')], max_length=2)),
                ('ultimo_mantenimiento', models.DateField(blank=True)),
                ('funcionando', models.BooleanField(default=True)),
                ('idmpresaExterna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empresaexterna_Maquinaria', to='ITV.empresaexterna')),
                ('iestacionItv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estacionitv_Maquinaria', to='ITV.estacionitv')),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('puesto', models.CharField(choices=[('EM', 'Emisiones'), ('FR', 'Frenos'), ('DI', 'Direccion')], max_length=2)),
                ('sueldo', models.FloatField()),
                ('observaciones', models.TextField()),
                ('estacion', models.ManyToManyField(related_name='estacionItv_trabajadores', to='ITV.estacionitv')),
            ],
        ),
        migrations.AddField(
            model_name='inspeccion',
            name='trabajador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trabajador_Inspeccion', to='ITV.trabajador'),
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_matriculacion', models.DateField()),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('numero_bastidor', models.CharField(max_length=17)),
                ('tipo_vehiculo', models.CharField(choices=[('tur', 'Turismo'), ('moto', 'Motocicleta'), ('cam', 'Camión'), ('bus', 'Autobús'), ('furg', 'Furgoneta'), ('quad', 'Quad'), ('tracto', 'Tractor')], max_length=6)),
                ('cilindrada', models.IntegerField()),
                ('potencia', models.IntegerField()),
                ('combustible', models.CharField(choices=[('gas', 'Gasolina'), ('die', 'Diésel'), ('ele', 'Eléctrico'), ('hib', 'Híbrido'), ('gpl', 'GLP (Gas Licuado)'), ('gnv', 'GNC (Gas Natural)')], max_length=3)),
                ('mma', models.PositiveIntegerField()),
                ('asientos', models.PositiveSmallIntegerField()),
                ('ejes', models.PositiveSmallIntegerField()),
                ('dni_propietario', models.CharField(max_length=9)),
                ('matricula', models.CharField(max_length=7)),
                ('trabajadores', models.ManyToManyField(related_name='trabajador_Vehiculo', through='ITV.Inspeccion', to='ITV.trabajador')),
            ],
        ),
        migrations.AddField(
            model_name='inspeccion',
            name='vehiculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehiculo_Inspeccion', to='ITV.vehiculo'),
        ),
    ]
