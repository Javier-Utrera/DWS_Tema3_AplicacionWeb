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
    path('clientes/buscar',views.buscar_cliente,name="buscar_cliente"),
    
    #Buscar inspeccion
    path('inspecciones/buscar',views.buscar_inspeccion,name="buscar_inspeccion"),
    
    #Buscar vehiculo 
    path('vehiculos/buscar',views.buscar_vehiculo,name="buscar_vehiculo"),
    
    #Buscar local
    path('locales/buscar',views.buscar_local,name="buscar_local"), 
    
    #Buscar estacion 
    path('estaciones/buscar',views.buscar_estacion,name="buscar_estacion"),
    
    #Buscar trabajador  
    path('trabajadores/buscar',views.buscar_trabajador,name="buscar_trabajador"),
    
        #ACTUALIZAR
    
    #Actualizar cliente
    path('clientes/editar/<int:cliente_id>', views.editar_cliente,name="editar_cliente"),
    
    #Actualizar inspeccion
    path('inspecciones/editar/<int:inspeccion_id>', views.editar_inspeccion,name="editar_inspeccion"),
    
    #Actualizar vehiculo
    path('vehiculos/editar/<int:vehiculo_id>', views.editar_vehiculo,name="editar_vehiculo"),
    
    #Actualizar local
    path('locales/editar/<int:local_id>', views.editar_local,name="editar_local"),
    
    #Actualizar estacion
    # path('estaciones/editar/<int:estacion_id>', views.editar_estacion,name="editar_estacion"),
    
    #Actualizar trabajador
    # path('trabajadores/editar/<int:trabajador_id>', views.editar_trabajador,name="editar_trabajador"),
]       