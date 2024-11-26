from django.urls import path
from django.contrib import admin
from .import views

urlpatterns = [
    path('', views.index,name="urls_index"),
    #1
    path('clientes/listar_clientes', views.listar_clientes,name="urls_listar_clientes"),
    
    #2
    path('citas/cita_cliente/<int:id_cliente>', views.cita_cliente,name="urls_cita_cliente"),
    
    #3
    path('estaciones/local_precio', views.estaciones_con_locales,name="urls_estaciones_con_locales"),
    
    #4
    path('trabajadores/trabajador_estacion/<int:id_estacion>', views.trabajadores_estacion,name="urls_trabajadores_estacion"),
    
    #5
    path('inspecciones', views.inspecciones_vehiculo,name="urls_inspecciones_vehiculo"),
    
    #6
    path('maquinarias/<int:id_maquina>', views.maquinaria_empresa,name="urls_maquinaria_empresa"),
    
    #7
    path('citas/<int:anio1>/<int:anio2>', views.citas_fechas,name="urls_citas_fechas"),
    
    #8
    path('vehiculos', views.contador_vehiculos_combustible,name="urls_vehiculos"),
    
    #9
    path('citas/citas_estacion/<int:id_cliente>/<str:tipo_inspeccion>', views.citas_estacion,name="urls_citas_estacion"),
    
    #10
    path('vehiculos/vehiculos_sin_trabajador', views.vehiculos_sin_trabajadores,name="urls_vehiculos_sin_trabajadores"),
    
    #11
    path('locales', views.locales,name="urls_locales"),
    
    
    #FOMULARIOS

    #Crear cliente
    path('clientes/create', views.procesar_cliente,name="urls_crear_cliente"),
    
    #Crear inspeccion
    path('inspecciones/create', views.procesar_inspeccion,name="urls_crear_inspeccion"),
    
    #Crear vehiculo
    path('vehiculos/create', views.procesar_vehiculo,name="urls_crear_inspeccion"),
    
    #Crear local
    path('locales/create', views.procesar_local,name="urls_crear_local"),
    
    #Crear estacion
    path('estaciones/create', views.procesar_estacion,name="urls_crear_estacion"),
    
    #Crear trabajador
    path('trabajadores/create', views.procesar_trabajador,name="urls_crear_trabajador"),
]       