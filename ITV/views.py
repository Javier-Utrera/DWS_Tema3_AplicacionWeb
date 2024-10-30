from django.shortcuts import render
from .models import *
from django.db.models import Q,Prefetch, Count
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
    citas=citas.filter(cliente_id=id_cliente).all()
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
def maquinaria_empresa(request,id_maquina):
    maquinarias=Maquinaria.objects.select_related("iestacionItv","idmpresaExterna")
    maquinarias=maquinarias.filter(id=id_maquina).get()
    return render(request,"maquinarias/maquinaria_empresa.html",{'views_maquinaria_empresa':maquinarias})

# Citas de las Estaciones en Rango de Fechas mostrando la cita mas reciente de ese rango
def citas_fechas(request,anio1,anio2):
    citas=Cita.objects.select_related("cliente","estacion")
    citas=citas.filter(fecha_propuesta__year__gte=anio1,fecha_propuesta__year__lte=anio2)
    citas=citas.order_by("-fecha_propuesta")[:1].get()
    return render(request,"citas/cita_estacion.html",{'views_cita_cliente':citas})

# Conteo de Vehículos por un tipo de combustible u otro: Número total de vehículos que sea 
def contador_vehiculos_combustible(request,combustible1,combustible2):
    vehiculos=Vehiculo.objects.prefetch_related("trabajadores",Prefetch("vehiculo_Inspeccion"))
    vehiculos=vehiculos.filter(Q(combustible=combustible1) | Q(combustible=combustible2)).all()
    contador=vehiculos.aggregate(Count("id"))
    return render(request,"vehiculos/contador_vehiculos.html",{'views_contador_vehiculos_combustible':vehiculos,'contador':contador})

# Muestra todas las citas de una estación ITV, filtradas por el ID del cliente y el tipo de inspección
def citas_estacion(request,id_cliente,tipo_inspeccion):
    citas=Cita.objects.select_related("cliente","estacion")
    citas=citas.filter(cliente_id=id_cliente,tipo_inspeccion=tipo_inspeccion).all()
    return render(request,"citas/citas_estacion.html",{'views_citas_estacion':citas})
    
# Vehículos sin Trabajadores Asociados: Vehículos que no tienen trabajadores asociados.
def vehiculos_sin_trabajadores(request):
    vehiculos=Vehiculo.objects.prefetch_related("trabajadores",Prefetch("vehiculo_Inspeccion"))
    vehiculos=vehiculos.filter(trabajadores=None).all()
    return render(request,"vehiculos/vehiculos_sin_trab.html",{'views_vehiculos_sin_trabajadores':vehiculos})

def mi_error_400(request,exception=None):
    return render(request,"errores/400.html",None,None,400)

def mi_error_403(request,exception=None):
    return render(request,"errores/403.html",None,None,403)

def mi_error_404(request,exception=None):
    return render(request,"errores/404.html",None,None,404)

def mi_error_500(request,exception=None):
    return render(request,"errores/500.html",None,None,500)