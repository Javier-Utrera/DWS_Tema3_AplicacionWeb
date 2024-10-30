from django.shortcuts import render
from .models import *
from django.db.models import Q,Prefetch
# Create your views here.
def index(request):
    return render(request,"index.html")

# Lista de Clientes: Todos los clientes filtrados por sexo, nombre y fecha de nacimiento.
def listar_clientes(request):
    clientes=Cliente.objects.order_by("sexo","nombre","fecha_nacimiento").all()
    return render(request,"clientes/listar_clientes.html",{'views_listar_cliente':clientes})

# Citas de un Cliente: Todas las citas de un cliente específico.
def cita_cliente(request,id_cliente):
    citas=Cita.objects.select_related("cliente","estacion")
    citas=citas.filter(cliente_id=id_cliente).get()
    return render(request,"citas/cita_cliente.html",{'views_cita_cliente':citas})
    
# Estaciones ITV con Locales: Estaciones ITV junto a su local, ordenadas por el precio del local.
def estaciones_con_locales(request):
    estaciones=EstacionItv.objects.select_related("local").order_by("local__precio").all()
    return render(request,"estaciones/estaciones_con_locales_ordenados.html",{'views_estaciones_con_locales':estaciones})

# Trabajadores de una Estación: todos los datos de los trabajadores de una estación ITV específica.
def trabajadores_estacion(request,id_estacion):
    estacion=EstacionItv.objects.get(id=id_estacion)
    trabajadores=Trabajador.objects.prefetch_related("estacion",
                                                     Prefetch("trabajador_Inspeccion"),
                                                     Prefetch("trabajador_Vehiculo"))
    trabajadores=trabajadores.filter(estacion=id_estacion).all()
    return render(request,"trabajadores/trabajadores_estacion_especifica.html",{'views_trabajadores_estacion':trabajadores,'estaciones':estacion})
# Inspecciones de un Vehículo: Inspecciones de un vehículo específico por matrícula.
def inspecciones_vehiculo(request,matricula):
    inspecciones=Inspeccion.objects.select_related("trabajador","vehiculo")
    inspecciones=inspecciones.filter(vehiculo__matricula=matricula).all()
    return render(request,"inspecciones/inspecciones_vehiculo.html",{'views_inspecciones_vehiculo':inspecciones})
# Detalle de una Maquinaria y Empresa: Detalle de una maquinaria específica y su empresa externa asociada.

# Citas de una Estación en Rango de Fechas: Citas de una estación ITV en un rango de fechas determinado.

# Conteo de Vehículos por Combustible: Número total de vehículos agrupados por tipo de combustible.

# Muestra todas las citas de una estación ITV, filtradas por el ID del cliente y el tipo de inspección

# Vehículos sin Trabajadores Asociados: Vehículos que no tienen trabajadores asociados.