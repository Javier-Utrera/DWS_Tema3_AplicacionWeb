from django.urls import path
from django.contrib import admin
from .import views

urlpatterns = [
    path('', views.index,name="urls_index"),
    #1
    path('clientes/listar_clientes', views.listar_clientes,name="listar_clientes"),
    
    #2
    path('citas/listar_citas', views.listar_citas,name="listar_citas"),
    
    #3
    path('estaciones/listar_estaciones', views.listar_estaciones,name="listar_estaciones"),
    
    #4
    path('trabajadores/listar_trabajadores', views.listar_trabajadores,name="listar_trabajadores"),
    
    #5
    path('inspecciones/listar_inspecciones', views.listar_inspecciones,name="listar_inspecciones"),
     
    #7
    path('vehiculos/listar_vehiculos', views.listar_vehiculos,name="listar_vehiculos"),
    
    #8
    path('locales/listar_locales', views.listar_locales,name="listar_locales"),
    
    
    #FOMULARIOS
    
        #CREATE

    #Crear cliente
    path('clientes/create', views.procesar_cliente,name="procesar_cliente"),
    
    #Crear inspeccion
    path('inspecciones/create', views.procesar_inspeccion,name="procesar_inspeccion"),
    
    #Crear vehiculo
    path('vehiculos/create', views.procesar_vehiculo,name="procesar_vehiculo"),
    
    #Crear local
    path('locales/create', views.procesar_local,name="procesar_local"),
    
    #Crear estacion
    path('estaciones/create', views.procesar_estacion,name="procesar_estacion"),
    
    #Crear trabajador
    path('trabajadores/create', views.procesar_trabajador,name="procesar_trabajador"),
    
        #BUSQUEDA AVANZADA
        
    #Buscar cliente
    
    path('clientes/buscar/',views.buscar_cliente,name="buscar_cliente"),   
]       