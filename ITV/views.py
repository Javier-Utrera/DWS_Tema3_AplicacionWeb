from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    return render(request,"index.html")

# Lista de Clientes: Todos los clientes filtrados por sexo, nombre y fecha de nacimiento.

# Citas de un Cliente: Todas las citas de un cliente específico.

# Estaciones ITV con Locales: Estaciones ITV junto a su local, ordenadas alfabéticamente.

# Trabajadores de una Estación: Trabajadores de una estación ITV específica.

# Inspecciones de un Vehículo: Inspecciones de un vehículo específico por matrícula.

# Detalle de una Maquinaria y Empresa: Detalle de una maquinaria específica y su empresa externa asociada.

# Citas de una Estación en Rango de Fechas: Citas de una estación ITV en un rango de fechas determinado.

# Conteo de Vehículos por Combustible: Número total de vehículos agrupados por tipo de combustible.

# Facturas no Pagadas: Facturas no pagadas, ordenadas por fecha de emisión descendente.

# Vehículos sin Trabajadores Asociados: Vehículos que no tienen trabajadores asociados.