from django.urls import path
from django.contrib import admin
from .import views

urlpatterns = [
    path('', views.index,name="urls_index"),
    path('clientes/listar_clientes', views.listar_clientes,name="urls_listar_clientes"),
    path('citas/cita_cliente/<int:id_cliente>', views.cita_cliente,name="urls_cita_cliente"),
    path('estaciones/local_precio', views.estaciones_con_locales,name="urls_estaciones_con_locales"),
    path('trabajadores/trabajador_estacion/<int:id_estacion>', views.trabajadores_estacion,name="urls_trabajadores_estacion"),
    path('inspecciones/<str:matricula>', views.inspecciones_vehiculo,name="urls_inspecciones_vehiculo"),
]   