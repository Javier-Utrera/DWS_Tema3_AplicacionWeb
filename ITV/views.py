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
        
    if len(request.GET)>0:
        formulario = BusquedaAvanzadaCliente(request.GET)
        if formulario.is_valid():
            mensaje="Se ha buscado los siguientes valores: \n"
            clientes=Cliente.objects.prefetch_related(Prefetch("cliente_Cita"))
            
            nombrev=formulario.cleaned_data.get("nombre")
            dniv=formulario.cleaned_data.get("dni") 
            fecha_nacimientov=formulario.cleaned_data.get("fecha_nacimiento")
            
            if(nombrev!=""):
                clientes=clientes.filter(nombre__contains=nombrev)
                mensaje+="Nombre que se ha buscado " + nombrev  +"\n"
            if(dniv!=""):
                clientes=clientes.filter(dni=dniv)
                mensaje+="Dni por el que se ha buscado " + dniv + "\n"
            if(not fecha_nacimientov is None):
                clientes=clientes.filter(fecha_nacimiento=fecha_nacimientov)
                mensaje+="La fecha por la que se esta buscando es" + datetime.strftime(fecha_nacimientov,'%d-%m-%Y')+"\n"
            
            clientes=clientes.all()
            
            return render(request,"clientes/listar_clientes.html",{
            "views_listar_cliente":clientes,
            "texto_busqueda":mensaje})
    
    else:
        formulario=BusquedaAvanzadaCliente(None)
    return render(request, 'clientes/busqueda_avanzada.html',{"formulario":formulario})
            
def editar_cliente(request,cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    
    datosFormulario = None
    archivosFormulario = None
    if request.method == "POST":
        datosFormulario = request.POST
        archivosFormulario = request.FILES
    
    
    formulario = ClienteForm(datosFormulario,archivosFormulario,instance = cliente)
    
    if (request.method == "POST"):
       
        if formulario.is_valid():
            try:  
                formulario.save()
                messages.success(request, 'Se ha editado el cliente '+formulario.cleaned_data.get('nombre')+" correctamente")
                return redirect('listar_clientes')  
            except Exception as error:
                print(error)
    return render(request, 'clientes/actualizar.html',{"formulario":formulario,"cliente":cliente})

def eliminar_cliente(request,cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    try:
        cliente.delete()
        messages.success(request, "Se ha elimnado el cliente "+cliente.nombre+" correctamente")
    except Exception as error:
        print(error)
    return redirect('listar_clientes')
            
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

def buscar_inspeccion(request):
        
    if len(request.GET)>0:
        formulario = BusquedaAvanzadaInspeccion(request.GET)
        if formulario.is_valid():
            mensaje="Se ha buscado los siguientes valores: \n"
            inspecciones=Inspeccion.objects.select_related("trabajador","vehiculo").prefetch_related(Prefetch("inspeccion_Factura"))
            
            resultado_inspeccionv=formulario.cleaned_data.get("resultado_inspeccion")
            notas_inspeccionv=formulario.cleaned_data.get("notas_inspeccion") 
            fecha_inspeccionv=formulario.cleaned_data.get("fecha_inspeccion") 
            
            if(resultado_inspeccionv !=""):
                inspecciones=inspecciones.filter(resultado_inspeccion__contains=resultado_inspeccionv)
                mensaje+="Texto que se ha buscado " + resultado_inspeccionv  +"\n"
            if(notas_inspeccionv!=""):
                inspecciones=inspecciones.filter(notas_inspeccion__contains=notas_inspeccionv)
                mensaje+="Texto de la inspeccion por el que se ha buscado " + notas_inspeccionv + "\n"
            if(not fecha_inspeccionv is None):
                inspecciones=inspecciones.filter(fecha_inspeccion=fecha_inspeccionv)
                mensaje+="La fecha por la que se esta buscando es" + datetime.strftime(fecha_inspeccionv,'%d-%m-%Y')+"\n"
            
            inspecciones=inspecciones.all()
            
            return render(request,"inspecciones/lista_inspecciones.html",{
            "views_inspecciones_vehiculo":inspecciones,
            "texto_busqueda":mensaje})
    
    else:
        formulario=BusquedaAvanzadaInspeccion(None)
    return render(request, 'inspecciones/busqueda_avanzada.html',{"formulario":formulario})


def editar_inspeccion(request,inspeccion_id):
    inspeccion = Inspeccion.objects.get(id=inspeccion_id)
    
    datosFormulario = None
    
    if request.method == "POST":
        datosFormulario = request.POST
    
    
    formulario = InspeccionForm(datosFormulario,instance = inspeccion)
    
    if (request.method == "POST"):
       
        if formulario.is_valid():
            try:  
                formulario.save()
                messages.success(request, 'Se ha editado la inspeccion '+formulario.cleaned_data.get('resultado_inspeccion')+" correctamente")
                return redirect('listar_inspecciones')  
            except Exception as error:
                print(error)
    return render(request, 'inspecciones/actualizar.html',{"formulario":formulario,"inspeccion":inspeccion})

def eliminar_inspeccion(request,inspeccion_id):
    inspeccion = Inspeccion.objects.get(id=inspeccion_id)
    try:
        inspeccion.delete()
        messages.success(request, "Se ha elimnado la inspeccion con el resultado "+inspeccion.resultado_inspeccion+" correctamente")
    except Exception as error:
        print(error)
    return redirect('listar_inspecciones')

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

def buscar_vehiculo(request):
        
    if len(request.GET)>0:
        formulario = BusquedaAvanzadaVehiculo(request.GET)
        if formulario.is_valid():
            mensaje="Se ha buscado los siguientes valores: \n"
            vehiculos=Vehiculo.objects.prefetch_related("trabajadores",Prefetch("vehiculo_Inspeccion"))
            
            marcav=formulario.cleaned_data.get("marca")
            potenciav=formulario.cleaned_data.get("potencia") 
            matriculav=formulario.cleaned_data.get("matricula") 
            
            if(marcav != ""):
                vehiculos=vehiculos.filter(marca=marcav)
                mensaje+="Marca que se ha buscado " + marcav  +"\n"
            if(potenciav!= ""):
                vehiculos=vehiculos.filter(potencia=potenciav)
                mensaje+="Inspeccion por el que se ha buscado " + str(potenciav) + "\n"
            if(matriculav!= ""):
                vehiculos=vehiculos.filter(matricula__contains=matriculav)
                mensaje+="Matricula que se esta buscando es" + matriculav +"\n"
            
            vehiculos=vehiculos.all()
            
            return render(request,"vehiculos/lista_vehiculos.html",{
            "views_vehiculos":vehiculos,
            "texto_busqueda":mensaje})
    
    else:
        formulario=BusquedaAvanzadaVehiculo(None)
    return render(request,'vehiculos/busqueda_avanzada.html',{"formulario":formulario})

def editar_vehiculo(request,vehiculo_id):
    vehiculo = Vehiculo.objects.get(id=vehiculo_id)
    
    datosFormulario = None
    
    if request.method == "POST":
        datosFormulario = request.POST
    
    
    formulario = VehiculoForm(datosFormulario,instance = vehiculo)
    
    if (request.method == "POST"):
       
        if formulario.is_valid():
            try:  
                formulario.save()
                messages.success(request, 'Se ha editado el vehiculo con matricula '+formulario.cleaned_data.get('matricula')+" correctamente")
                return redirect('listar_vehiculos')  
            except Exception as error:
                print(error)
    return render(request, 'vehiculos/actualizar.html',{"formulario":formulario,"vehiculo":vehiculo})

def eliminar_vehiculo(request,vehiculo_id):
    vehiculo = Vehiculo.objects.get(id=vehiculo_id)
    try:
        vehiculo.delete()
        messages.success(request, "Se ha elimnado el vehiculo con matricula "+vehiculo.matricula+" correctamente")
    except Exception as error:
        print(error)
    return redirect('listar_vehiculos')

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

def buscar_local(request):
        
    if len(request.GET)>0:
        formulario = BusquedaAvanzadaLocal(request.GET)
        if formulario.is_valid():
            mensaje="Se ha buscado los siguientes valores: \n"
            locales=Local.objects
            
            preciov=formulario.cleaned_data.get("precio")
            metrosv=formulario.cleaned_data.get("metros") 
            anio_arrendamientov=formulario.cleaned_data.get("anio_arrendamiento") 
            
            if(not preciov is None):
                locales=locales.filter(precio=preciov)
                mensaje+="Precio que se ha buscado " + str(preciov)  +"\n"
            if(not metrosv is None):
                locales=locales.filter(metros=metrosv)
                mensaje+="Metros por el que se ha buscado " + str(metrosv) + "\n"
            if(not anio_arrendamientov is None):
                locales=locales.filter(anio_arrendamiento=anio_arrendamientov)
                mensaje+="La fecha por la que se esta buscando es" +  datetime.strftime(anio_arrendamientov,'%d-%m-%Y')+"\n"
            
            locales=locales.all()
            
            return render(request,"locales/listar_local.html",{
            "views_locales":locales,
            "texto_busqueda":mensaje})
    
    else:
        formulario=BusquedaAvanzadaLocal(None)
    return render(request,'locales/busqueda_avanzada.html',{"formulario":formulario})

def editar_local(request,local_id):
    local = Local.objects.get(id=local_id)
    
    datosFormulario = None
    
    if request.method == "POST":
        datosFormulario = request.POST
    
    
    formulario = LocalForm(datosFormulario,instance = local)
    
    if (request.method == "POST"):
       
        if formulario.is_valid():
            try:  
                formulario.save()
                messages.success(request, 'Se ha editado el local con el dueño '+formulario.cleaned_data.get('duenio')+" correctamente")
                return redirect('listar_locales')  
            except Exception as error:
                print(error)
    return render(request, 'locales/actualizar.html',{"formulario":formulario,"local":local})

def eliminar_local(request,local_id):
    local = Local.objects.get(id=local_id)
    try:
        local.delete()
        messages.success(request, "Se ha elimnado el local con el dueño "+local.duenio+" correctamente")
    except Exception as error:
        print(error)
    return redirect('listar_locales')

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

def buscar_estacion(request):
        
    if len(request.GET)>0:
        formulario = BusquedaAvanzadaEstacion(request.GET)
        if formulario.is_valid():
            mensaje="Se ha buscado los siguientes valores: \n"
            estaciones=EstacionItv.objects.select_related("local").prefetch_related(Prefetch("estacionitv_Cita"),
                                                                                    Prefetch("estacionitv_Maquinaria"),
                                                                                    Prefetch("estacionItv_trabajadores"),)
            
            nombrev=formulario.cleaned_data.get("nombre")
            munipiov=formulario.cleaned_data.get("munipio") 
            comunidad_autonomav=formulario.cleaned_data.get("comunidad_autonoma") 
            
            if(nombrev != ""):
                estaciones=estaciones.filter(nombre__contains=nombrev)
                mensaje+="Texto que se ha buscado " + nombrev  +"\n"
            if(munipiov != ""):
                estaciones=estaciones.filter(munipio=munipiov)
                mensaje+="Municipio que se ha buscado " + munipiov + "\n"
            if(comunidad_autonomav != ""):
                estaciones=estaciones.filter(comunidad_autonoma=comunidad_autonomav)
                mensaje+="Comunidad autonoma que se esta buscando es" +  comunidad_autonomav+"\n"
            
            estaciones=estaciones.all()
            
            return render(request,"estaciones/listar_estaciones.html",{
            "views_estaciones_con_locales":estaciones,
            "texto_busqueda":mensaje})
    
    else:
        formulario=BusquedaAvanzadaEstacion(None)
    return render(request,'estaciones/busqueda_avanzada.html',{"formulario":formulario})

def editar_estacion(request,estacion_id):
    estacion = EstacionItv.objects.get(id=estacion_id)
    
    datosFormulario = None
    
    if request.method == "POST":
        datosFormulario = request.POST
    
    
    formulario = EstacionForm(datosFormulario,instance = estacion)
    
    if (request.method == "POST"):
       
        if formulario.is_valid():
            try:  
                formulario.save()
                messages.success(request, 'Se ha editado la estacion con el nombre '+formulario.cleaned_data.get('nombre')+" correctamente")
                return redirect('listar_estaciones')  
            except Exception as error:
                print(error)
    return render(request, 'estaciones/actualizar.html',{"formulario":formulario,"estacion":estacion})

def eliminar_estacion(request,estacion_id):
    estacion = EstacionItv.objects.get(id=estacion_id)
    try:
        estacion.delete()
        messages.success(request, "Se ha elimnado la estacion con el nombre "+estacion.nombre+" correctamente")
    except Exception as error:
        print(error)
    return redirect('listar_estaciones')

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

def buscar_trabajador(request):
        
    if len(request.GET)>0:
        formulario = BusquedaAvanzadaTrabajador(request.GET)
        if formulario.is_valid():
            mensaje="Se ha buscado los siguientes valores: \n"
            trabajadores=Trabajador.objects.prefetch_related("estacion",
                                                     Prefetch("trabajador_Inspeccion"),
                                                     Prefetch("trabajador_Vehiculo"))
            
            nombrev=formulario.cleaned_data.get("nombre")
            sueldov=formulario.cleaned_data.get("sueldo") 
            puestov=formulario.cleaned_data.get("puesto") 
            
            if(nombrev != ""):
                trabajadores=trabajadores.filter(nombre__contains=nombrev)
                mensaje+="Texto que se ha buscado " + nombrev  +"\n"
            if(not sueldov is None):
                trabajadores=trabajadores.filter(sueldo=sueldov)
                mensaje+="Sueldo que se ha buscado " + str(sueldov) + "\n"
            if(puestov != ""):
                trabajadores=trabajadores.filter(puesto=puestov)
                mensaje+="Puesto que se esta buscando es" +  puestov+"\n"
            
            trabajadores=trabajadores.all()
            
            return render(request,"trabajadores/listar_trabajadores.html",{
            "views_trabajadores_estacion":trabajadores,
            "texto_busqueda":mensaje})
    
    else:
        formulario=BusquedaAvanzadaTrabajador(None)
    return render(request,'trabajadores/busqueda_avanzada.html',{"formulario":formulario})

def editar_trabajador(request,trabajador_id):
    trabajador = Trabajador.objects.get(id=trabajador_id)
    
    datosFormulario = None
    
    if request.method == "POST":
        datosFormulario = request.POST
    
    
    formulario = TrabajadorForm(datosFormulario,instance = trabajador)
    
    if (request.method == "POST"):
       
        if formulario.is_valid():
            try:  
                formulario.save()
                messages.success(request, 'Se ha editado el trabajador con el nombre '+formulario.cleaned_data.get('nombre')+" correctamente")
                return redirect('listar_trabajadores')  
            except Exception as error:
                print(error)
    return render(request, 'trabajadores/actualizar.html',{"formulario":formulario,"trabajador":trabajador})

def eliminar_trabajador(request,trabajador_id):
    trabajador = Trabajador.objects.get(id=trabajador_id)
    try:
        trabajador.delete()
        messages.success(request, "Se ha elimnado el trabajador con el nombre "+trabajador.nombre+" correctamente")
    except Exception as error:
        print(error)
    return redirect('listar_trabajadores')