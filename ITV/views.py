from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    return render(request,"index.html")

# 1. Listar clientes y sus citas, incluyendo información detallada sobre las inspecciones realizadas para cada cita.

# 2. Mostrar un trabajador específico y todos los vehículos inspeccionados, utilizando la relación intermedia Inspeccion.

# 3. Listar estaciones ITV en una comunidad autónoma específica, ordenadas por eficiencia energética.

# 4. Mostrar información de un vehículo y sus inspecciones, incluyendo detalles de los trabajadores asociados a cada inspección.

# 5. Listar maquinarias de un tipo específico y/o con mantenimiento reciente.

# 6. Listar facturas, separadas en pagadas y pendientes, mostrando los detalles de cada inspección asociada.

# 7. Mostrar estadísticas de inspección por comunidad autónoma, incluyendo el número de inspecciones y el importe promedio.

# 8. Mostrar detalles de una cita específica, incluyendo información de cliente y estación ITV asociada.

# 9. Listar trabajadores y las estaciones de ITV en las que trabajan, limitando el número de resultados.

# 10. Listar empresas externas y el coste total de las maquinarias asignadas a cada una.

