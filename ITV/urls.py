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
    path('inspecciones/<str:matricula>', views.inspecciones_vehiculo,name="urls_inspecciones_vehiculo"),
    
    #6
    path('maquinarias/<int:id_maquina>', views.maquinaria_empresa,name="urls_maquinaria_empresa"),
    
    #7
    path('citas/<int:anio1>/<int:anio2>', views.citas_fechas,name="urls_citas_fechas"),
    
    #8
    path('vehiculos/vehiculo_contador/<str:combustible1>/<str:combustible2>', views.contador_vehiculos_combustible,name="urls_contador_vehiculos_combustible"),
    
    #9
    path('citas/citas_estacion/<int:id_cliente>/<str:tipo_inspeccion>', views.citas_estacion,name="urls_citas_estacion"),
    
    #10
    path('vehiculos/vehiculos_sin_trabajador', views.vehiculos_sin_trabajadores,name="urls_vehiculos_sin_trabajadores"),
]       