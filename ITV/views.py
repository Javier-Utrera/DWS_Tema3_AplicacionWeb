from django.shortcuts import render
from .models import *
from .forms import *
from django.db.models import Q,Prefetch
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"index.html")

# 1 
def listar_clientes(request):
    clientes=Cliente.objects.prefetch_related(Prefetch("cliente_Cita")).all()
    return render(request,"clientes/listar_clientes.html",{'views_listar_cliente':clientes})

# 2 
def listar_citas(request):
    citas=Cita.objects.select_related("cliente","estacion").all() 
    return render(request,"citas/listar_citas.html",{'views_citas':citas})
    
# 3 
def listar_estaciones(request):
    estaciones=EstacionItv.objects.select_related("local").prefetch_related(Prefetch("estacionitv_Cita"),
                                                                            Prefetch("estacionitv_Maquinaria"),
                                                                            Prefetch("estacionItv_trabajadores"),).all()
    return render(request,"estaciones/listar_estaciones.html",{'views_estaciones_con_locales':estaciones})

# 4 
def listar_trabajadores(request):
    trabajadores=Trabajador.objects.prefetch_related("estacion",
                                                     Prefetch("trabajador_Inspeccion"),
                                                     Prefetch("trabajador_Vehiculo")).all()
    return render(request,"trabajadores/listar_trabajadores.html",{'views_trabajadores_estacion':trabajadores})

# 5 
def listar_inspecciones(request):
    inspecciones=Inspeccion.objects.select_related("trabajador","vehiculo").prefetch_related(Prefetch("inspeccion_Factura")).all()
    return render(request,"inspecciones/listar_inspecciones.html",{'views_inspecciones_vehiculo':inspecciones})

# 7 
def listar_vehiculos(request):
    vehiculos=Vehiculo.objects.prefetch_related("trabajadores",Prefetch("vehiculo_Inspeccion")).all()
    return render(request,"vehiculos/listar_vehiculos.html",{'views_vehiculos':vehiculos})
    
# 8
def listar_locales(request):
    locales=Local.objects.all()
    return render(request,"locales/listar_local.html",{'views_locales':locales})

def mi_error_400(request,exception=None):
    return render(request,"errores/400.html",None,None,400)

def mi_error_403(request,exception=None):
    return render(request,"errores/403.html",None,None,403)

def mi_error_404(request,exception=None):
    return render(request,"errores/404.html",None,None,404)

def mi_error_500(request,exception=None):
    return render(request,"errores/500.html",None,None,500)

#FORMULARIOS

#CLIENTE------------------------------

def procesar_cliente(request):
    if (request.method == "POST"):
        formulario=ClienteForm(request.POST)
        if formulario.is_valid():
            try:
                formulario.save()
                return redirect("listar_clientes")
            except Exception as error:
                print(error)
    else:
        formulario=ClienteForm()             
    return render(request,'clientes/create.html',{"formulario":formulario})

def buscar_cliente(request):
    formulario = BusquedaAvanzadaCliente(request.GET)
    
    if formulario.is_valid():
        texto=formulario.cleaned_data.get("textoBusqueda")
        cliente=Cliente.objects.prefetch_related(Prefetch("cliente_Cita"))
        cliente=cliente.filter(Q(nombre__contains=texto)| Q(dni__contains=texto)).all()
        return render(request,'clientes/lista_buscar.html',{"views_listar_cliente":cliente,"texto_busqueda":texto})
    if("HTTP_REFERER" in request.META):
        return redirect(request.META["HTTP_REFERER"])
    else:
        return redirect("urls_index")
#INSPECCION------------------------------
       
def procesar_inspeccion(request): 
    if (request.method == "POST"):
        formulario=InspeccionForm(request.POST)
        if formulario.is_valid():
            try:
                formulario.save()
                return redirect("listar_inspecciones")
            except Exception as error:
                print(error)
    else:
        formulario=InspeccionForm()  
    return render(request,'inspecciones/create.html',{"formulario":formulario})



#VEHICULO------------------------------
    
def procesar_vehiculo(request):
    if (request.method == "POST"):
        formulario=VehiculoForm(request.POST)
        if formulario.is_valid():
            try:
                formulario.save()
                return redirect("listar_vehiculos")
            except Exception as error:
                print(error)
    else:
        formulario=VehiculoForm()          
    return render(request,'vehiculos/create.html',{"formulario":formulario})

#LOCAL------------------------------

def procesar_local(request):
    if(request.method=="POST"):
        formulario=LocalForm(request.POST)
        if formulario.is_valid():
            try:
                formulario.save()
                return redirect("listar_locales")
            except Exception as error:
                print(error)
    else:
        formulario=LocalForm()
    return render(request,'locales/create.html',{"formulario":formulario})

#ESTACION------------------------------

def procesar_estacion(request):
    if(request.method=="POST"):
        formulario=EstacionForm(request.POST)
        if formulario.is_valid():
            try:
                formulario.save()
                return redirect("listar_estaciones")
            except Exception as error:
                print(error)
    else:
        formulario=EstacionForm()
    return render(request,'estaciones/create.html',{"formulario":formulario})

#TRABAJADOR------------------------------

def procesar_trabajador(request):
    if(request.method=="POST"):
        formulario=TrabajadorForm(request.POST)
        if formulario.is_valid():
            try:
                formulario.save()
                return redirect("listar_trabajadores")
            except Exception as error:
                print(error)
    else:
        formulario=TrabajadorForm()
    return render(request,'trabajadores/create.html',{"formulario":formulario})