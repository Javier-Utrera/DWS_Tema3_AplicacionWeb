from django.shortcuts import render
from .models import *
from .forms import *
from django.db.models import Q,Prefetch
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"index.html")

# 1 Lista de Clientes: Todos los clientes filtrados por sexo, nombre y fecha de nacimiento.
def listar_clientes(request):
    clientes=Cliente.objects.prefetch_related(Prefetch("cliente_Cita")) # me genera 2 queries
    clientes=clientes.order_by("sexo","nombre","fecha_nacimiento").all()
    return render(request,"clientes/listar_clientes.html",{'views_listar_cliente':clientes})

# 2 Citas de un Cliente: Todas las citas de un cliente específico. 
def cita_cliente(request,id_cliente):
    citas=Cita.objects.select_related("cliente","estacion") # me genera 1 queries
    citas=citas.filter(cliente_id=id_cliente).all()
    return render(request,"citas/listar_citas.html",{'views_citas':citas})
    
# 3 Estaciones ITV con Locales: Estaciones ITV junto a su local, ordenadas por el precio del local.
def estaciones_con_locales(request):
    estaciones=EstacionItv.objects.select_related("local").prefetch_related(Prefetch("estacionitv_Cita"),
                                                                            Prefetch("estacionitv_Maquinaria"),
                                                                            Prefetch("estacionItv_trabajadores"),)
    estaciones=estaciones.order_by("local__precio").all()
    return render(request,"estaciones/listar_estaciones.html",{'views_estaciones_con_locales':estaciones})

# 4 Trabajadores de una Estación: todos los datos de los trabajadores de una estación ITV específica.
def trabajadores_estacion(request,id_estacion):
    trabajadores=Trabajador.objects.prefetch_related("estacion",
                                                     Prefetch("trabajador_Inspeccion"),
                                                     Prefetch("trabajador_Vehiculo"))
    trabajadores=trabajadores.filter(estacion=id_estacion).all()
    return render(request,"trabajadores/listar_trabajadores.html",{'views_trabajadores_estacion':trabajadores})

# 5 Inspecciones de un Vehículo: Inspecciones de un vehículo específico por matrícula.
def inspecciones_vehiculo(request,matricula):
    inspecciones=Inspeccion.objects.select_related("trabajador","vehiculo").prefetch_related(Prefetch("inspeccion_Factura"))
    inspecciones=inspecciones.filter(vehiculo__matricula=matricula).all()
    return render(request,"inspecciones/listar_inspecciones.html",{'views_inspecciones_vehiculo':inspecciones})

# 6 Detalle de una Maquinaria y Empresa: Detalle de una maquinaria específica y su empresa externa asociada.
def maquinaria_empresa(request,id_maquina):
    maquinarias=Maquinaria.objects.select_related("iestacionItv","idmpresaExterna")
    maquinarias=maquinarias.filter(id=id_maquina).get()
    return render(request,"maquinarias/maquinaria_empresa.html",{'views_maquinaria_empresa':maquinarias})

# 7 Citas de las Estaciones en Rango de Fechas mostrando la cita mas reciente de ese rango 
def citas_fechas(request,anio1,anio2):
    citas=Cita.objects.select_related("cliente","estacion") 
    citas=citas.filter(fecha_propuesta__year__gte=anio1,fecha_propuesta__year__lte=anio2)
    citas=citas.order_by("-fecha_propuesta")[:1].get()
    return render(request,"citas/cita_fecha.html",{'views_citas_fechas':citas})

# 8 Conteo de Vehículos por un tipo de combustible u otro: Número total de vehículos que sea 
def contador_vehiculos_combustible(request,combustible1,combustible2):
    vehiculos=Vehiculo.objects.prefetch_related("trabajadores",Prefetch("vehiculo_Inspeccion"))
    vehiculos=vehiculos.filter(Q(combustible=combustible1) | Q(combustible=combustible2)).all()
    return render(request,"vehiculos/listar_vehiculos.html",{'views_vehiculos':vehiculos})

# 9 Muestra todas las citas de una estación ITV, filtradas por el ID del cliente y el tipo de inspección 
def citas_estacion(request,id_cliente,tipo_inspeccion):
    citas=Cita.objects.select_related("cliente","estacion")
    citas=citas.filter(cliente_id=id_cliente,tipo_inspeccion=tipo_inspeccion).all()
    return render(request,"citas/listar_citas.html",{'views_citas':citas})
    
#10 Vehículos sin Trabajadores Asociados: Vehículos que no tienen trabajadores asociados.
def vehiculos_sin_trabajadores(request):
    vehiculos=Vehiculo.objects.prefetch_related("trabajadores")
    vehiculos=vehiculos.filter(trabajadores=None).all()
    return render(request,"vehiculos/listar_vehiculos.html",{'views_vehiculos':vehiculos})

def mi_error_400(request,exception=None):
    return render(request,"errores/400.html",None,None,400)

def mi_error_403(request,exception=None):
    return render(request,"errores/403.html",None,None,403)

def mi_error_404(request,exception=None):
    return render(request,"errores/404.html",None,None,404)

def mi_error_500(request,exception=None):
    return render(request,"errores/500.html",None,None,500)

#FORMULARIOS

    #CLIENTE

def procesar_cliente(request):
    datosFormulario=None
    if request.method == "POST":
        datosFormulario = request.POST
        
    formulario=ClienteForm(datosFormulario)
    
    if (request.method== "POST"):
        cliente_creado=crear_cliente(formulario)
        if(cliente_creado):
            return redirect("urls_listar_clientes")
    return render(request,'clientes/create.html',{"formulario":formulario})

def crear_cliente(formulario):
    cliente_creado=False
    
    if formulario.is_valid():
        
        cliente= Cliente.objects.create(
                nombre=formulario.cleaned_data.get('nombre'),
                apellidos=formulario.cleaned_data.get('apellidos'),
                sexo=formulario.cleaned_data.get('sexo'),
                fecha_nacimiento=formulario.cleaned_data.get('fecha_nacimiento'),
                codigo_postal=formulario.cleaned_data.get('codigo_postal'),
                domicilio=formulario.cleaned_data.get('domicilio'),
                correo= formulario.cleaned_data.get('correo'),
                telefono=formulario.cleaned_data.get('telefono'),
                dni=formulario.cleaned_data.get('dni'),
        )       
        try:
            cliente.save()
            cliente_creado=True
        except:
            pass
    return cliente_creado

    #Inspeccion   
def procesar_inspeccion(request): 
    datosFomulario=None
    if (request.method == "POST"):
        datosFomulario=request.POST
        
    formulario=InspeccionForm(datosFomulario)
    
    if(request.method == "POST"):
        inspeccion_creado=crear_inspeccion(formulario)
        if(inspeccion_creado):
            return redirect("urls_inspecciones_vehiculo")
    return render(request,'inspecciones/create.html',{"formulario":formulario})

def crear_inspeccion(formulario):
    inspeccion_creado=False
    
    if formulario.is_valid():
        inspeccion = Inspeccion.objects.create(
            fecha_inspeccion = formulario.cleaned_data.get('fecha_inspeccion'),
            resultado_inspeccion = formulario.cleaned_data.get('resultado_inspeccion'), 
            notas_inspeccion = formulario.cleaned_data.get('notas_inspeccion'), 
            cliente_puntual = formulario.cleaned_data.get('cliente_puntual'),
            trabajador = formulario.cleaned_data.get('trabajador'),
            vehiculo = formulario.cleaned_data.get('vehiculo'),
        )
        
        try:
            inspeccion.save()
            inspeccion_creado=True
        except:
            pass
    return inspeccion_creado