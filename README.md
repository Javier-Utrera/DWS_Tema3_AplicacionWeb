# DWS_Tema3_AplicacionWeb

# Explicacion de mi aplicacion web

Esta aplicacion esta enfocada en la gestion del servicio ITV a nivel autonómico, para ello un cliente que no necesariamente tiene que ser el dueño del vehiculo que va ser inspeccionado, pide una cita en la itv que desee, su vehiculo sera inspeccionado por los trabajadores generando un resultado de la inspeccion y su correspondiente factura para su pago.

# Explicacion de los modelos, atributos y parametros
Modelo: Cliente
    Modelo que representa a los clientes de la ITV.

    Atributos:

        nombre: Campo de tipo CharField con un máximo de 50 caracteres, almacena el nombre del cliente.

        apellidos: Campo de tipo CharField (cadena) con un máximo de 50 caracteres. El parámetro (blank=True) indica que este campo es opcional. (No va ser necesario almacenar el apellido del cliente)

        sexo: Campo CharField que almacena un valor de 1 carácter. Se utilizan el parametro (choices) para especificar si es 'Masculino' o 'Femenino', en la base de datos se guarda como "M" o una "F". 

        fecha_nacimiento: Campo de tipo DateField, que almacena la fecha de nacimiento del cliente.

        codigo_postal: Campo IntegerField, almacena el código postal.

        domicilio: Campo TextField que puede almacenar texto largo, representa la dirección del cliente.

        correo: Campo EmailField, que almacena una dirección de correo electrónico con validación automática de formato.

        telefono: Campo PositiveIntegerField, almacena un número de teléfono (solo valores positivos).

        dni: Campo CharField de 9 caracteres, que almacena el DNI del cliente. El modificador unique=True asegura que cada DNI sea único en la base de datos.

        dueño: Campo Charfield de 50 caracteres donde almacena el dueño del local.

Modelo: Local

    Modelo que representa la información de los locales donde se puede establecer una estación ITV.

    Atributos:

        precio: Campo FloatField, almacena el precio del alquiler del local.

        metros: Campo DecimalField con un máximo de 50 dígitos y 3 decimales, que almacena el tamaño en metros cuadrados.

        anio_arrendamiento: Campo DateField, almacena el año en que se arrendó el local.

Modelo: EstacionItv

    Modelo las estaciones ITV.

    Relaciones:

        (ONETOONE,cada Estacion esta relacionada con un unico local)id_local: Relación OneToOneField con el modelo Local. La opción on_delete=models.CASCADE indica que si se elimina un local, también se eliminará la estación asociada.

    Atributos:

        nombre: Campo CharField de 50 caracteres, almacena el nombre de la estación. El modificador unique=True asegura que el nombre sea único.
        
        municipio: Campo CharField de 50 caracteres, almacena el municipio donde está la estación.

        eficiencia_energetica: Campo CharField que almacena un código de un carácter (como A, B, C...) para indicar la eficiencia energética.

        comunidad_autonoma: Campo CharField que almacena la comunidad autonoma donde se encuentra la estacion

Modelo: Cita

    Modelo que representa las citas para la inspección de vehículos.

    Relaciones:

        (MANYTOONE,un cliente puede tener varias citas)id_cliente: Relación ForeignKey con el modelo Cliente, establece que una cita está asociada con un cliente. La opción on_delete=models.CASCADE indica que si se elimina el cliente, se eliminan también las citas asociadas.

        (MANYTOONE,una itv puede tener varias citas)id_estacion: Relación ForeignKey con EstacionItv, indica la estación donde se realizará la inspección.

    Atributos:

        matricula: Campo CharField de 7 caracteres, almacena la matrícula del vehículo.
        
        fecha_matriculacion: Campo DateField, almacena la fecha de matriculación del vehículo. Utiliza el parametro (help_text) para mostrar una indicación adicional al usuario.
        
        numero_bastidor: Campo CharField de 17 caracteres, almacena el número de bastidor del vehículo.
        
        tipo_inspeccion: Campo CharField que almacena el tipo de inspección a realizar, utilizando el parametro (choices) con las opciones: 'Periodica', 'NoPeriodica', 'VerificacionTaximetro', etc. Almacena 'PE','NOPE','VETAX' etc..
        
        remolque: Campo BooleanField, que indica si el vehículo lleva o no remolque. Con el parametro (default=false) le indico que por defecto el vehiculo no lleva remolque
        
        tipo_pago: Campo CharField que define el método de pago (tarjeta o efectivo) usando el parametro (choices).
        
        fecha_propuesta: Campo DateField, fecha propuesta para la cita.
        
        hora_propuesta: Campo TimeField, hora propuesta para la cita.

Modelo: EmpresaExterna

    Modelo que representa a las empresas externas que mantienen las maquinas de la ITV.

    Atributos:

        nombre: Campo CharField, almacena el nombre de la empresa.

        municipio: Campo CharField, almacena el municipio donde está la empresa.

        coste: Campo FloatField, almacena el coste del servicio de la empresa, contiene el atributo (editable=true) para que este valor se pueda cambiar a posterior.

        cif: Campo CharField, almacena el CIF de la empresa.

Modelo: Maquinaria

    Modelo que representa la maquinaria usada en las estaciones ITV.

    Relaciones:

        (MANYTOONE,la itv contiene muchas maquinas, pero cada maquina solo puede estar en una ITV)id_estacionItv: Relación ForeignKey con EstacionItv, indica en qué estación se encuentra la maquinaria.

        (ONETOONE,cada empresa externa se especializa en un tipo de maquinaria)id_empresaExterna: Relación OneToOneField con EmpresaExterna, indica qué empresa provee o gestiona la maquinaria.

    Atributos:

        nombre: Campo CharField, almacena el nombre de la máquina.

        tipo: Campo CharField con el parametro (choices) para especificar el tipo de maquinaria (emisiones, frenos, dirección).

        ultimo_mantenimiento: Campo DateField, almacena la fecha del último mantenimiento. blank=True indica que es opcional.

        funcionando: Campo en el que por defecta es True, nos indica si la maquina esta en funcionamiento

Modelo: Trabajador

    Modelo que representa a los trabajadores de las estaciones ITV.

    En este modelo he intentado hacer una relacion recursiva MANYTOMANY consigo misma, ya que un trabajador puede ser jefe de varios empleados, y un mismo empleado puede tener varios jefes, no he conseguido hacerla funcionar son el seeder, pero al hacer el migrations no me salta ningun error

    Relaciones:

        (MANYTOMANY,un trabajador puede trabajar en varias estaciones y una estacion puede tener varios trabajadores)id_estacion: Relación ManyToManyField con EstacionItv, indica en qué estaciones trabaja el empleado.

        (MANYTOMANY)jefe: Relación recursiva ManyToManyField que permite establecer una jerarquía entre trabajadores (un trabajador puede tener un jefe o subordinados).
            Aqui he introducido 'self', ya que si llamaba a mi misma tabla me decia que no estaba definidica, con esto se llama a si misma como el .this de java.
            He especificado que puede estar vacio, ya que puede ser que un trabajador no tenga jefe
            Le he dado un related name por si evitaba el fallo del seed pero no he tenido suerte
            El parametro symetrical lo he encontrado en foros con personas que le ocurria mi problema, y le recomendaban ponerlo, creo entender que lo que evita es que no tenga que tener siembre el mismo numero de empleados un trabajador jefe

    Atributos:

        nombre: Campo CharField, almacena el nombre del trabajador.

        apellidos: Campo CharField, almacena los apellidos.

        puesto: Campo CharField que utiliza choices del modelo Maquinaria para especificar el tipo de trabajo que realiza el trabajador (según la maquinaria que use).
        
        sueldo: Campo FloatField, almacena el sueldo.
       
        observaciones: Campo TextField, almacena información adicional.

Modelo: Vehiculo

    Modelo que representa a los vehículos que pasan por la inspección.

    Relaciones:

        trabajadores: Relación ManyToManyField con Trabajador a través del modelo intermedio Inspeccion.

    Atributos:

        fecha_matriculacion: Campo tipo Date, Fecha de matriculación del vehículo.
        
        marca, modelo, numero_bastidor: Campos CharField que describen la marca, el modelo y el número de bastidor.
        
        tipo_vehiculo: Campo CharField que utiliza el parametro (choices) para definir el tipo de vehículo (turismo, camión, etc.).
        
        cilindrada: Campo IntegerField que almacena la cilindrada en cm³.
        
        potencia: Campo IntegerField Potencia del motor en CV.
        
        combustible: Tipo de combustible, usando choices (gasolina, diésel, eléctrico, etc.).
        
        mma: Campo PositiveIntegerField Masa Máxima Autorizada.
        
        asientos,ejes: Campo PosisiveSmallIntegerField Número de asientos y de ejes, este campo lo uso para ahorrar memoria, ya que no se va almacenar numeros muy grandes
        
        dni_propietario: DNI del propietario.
        
        matricula: Matrícula del vehículo.

Modelo: Inspeccion
    
    Modelo representa la inspección realizada,esta tabla es generada por una relacion MANYTOMANY entre trabajadores y vehiculos. le he añadido dos atributos propios.

    Relaciones:

        trabajador: Relación ForeignKey con Trabajador, indica quién realizó la inspección.

        vehiculo: Relación ForeignKey con Vehiculo, indica el vehículo inspeccionado.

    Atributos:

        fecha_inspeccion: Fecha en la que se realizó la inspección, con valor por defecto el día actual (timezone.now).
        
        resultado_inspeccion: Campo Charfield donde Resultado de la inspección

        notas_inspeccion: Campo Text en el que se almacena indicaciones o comentarios relevantes en inspeccion

        cliente_puntual: Campo Boolean con parametro "default=True", almacena si el cliente ha sido puntual

Modelo: Factura

    Modelo representa las facturas generadas.

    Relaciones:

        id_inspeccion: Relación OneToOneField con Inspeccion, cada inspección genera una factura.
        
        resultado: Relación OneToOneField con Inspeccion, usando un related_name ya que estoy relacionando en una misma tabla, la tabla Inspeccion 2 veces.

    Atributos:
        importe: Importe de la factura, almacenado como DecimalField.
        
        pagado: Campo BooleanField para indicar si se ha pagado la factura.

        fecha_emision_factura: Campo date para indicar cuando se emite la factura

        observaciones: Campo Text en el que se almacena indicaciones o comentarios relevantes en la factura


VISTAS:
    
1. Lista de Clientes
    Lista todos los clientes, ordenados por sexo, nombre y fecha de nacimiento.	
    Relación ManyToOne, order_by, carga optimizada con prefetch_related.

2. Citas de un Cliente	
    Muestra todas las citas de un cliente específico.	
    Parámetro entero, relación ManyToOne (cliente, estacion), select_related.

3. Estaciones con Locales	
    Lista las estaciones junto a su local, ordenadas por el precio del local.	
    Relación OneToOne y ManyToMany, order_by, select_related, prefetch_related.

4. Trabajadores de Estación	
    Muestra los trabajadores de una estación específica.	
    Parámetro entero, relaciones ManyToMany, prefetch_related.

5. Inspecciones de Vehículo	
    Lista todas las inspecciones de un vehículo usando la matrícula.	
    Parámetro str, relación ManyToOne, select_related, prefetch_related.

6. Maquinaria y Empresa	
    Muestra el detalle de una maquinaria y su empresa externa asociada.	
    Parámetro entero, relación OneToOne, select_related.

7. Citas por Rango de Fechas	
    Muestra la cita más reciente dentro de un rango de años.	
    Dos parámetros, AND, order_by, relación ManyToOne.

8. Conteo de Vehículos	
    Cuenta vehículos por dos tipos de combustible.	
    Filtro OR, aggregate, ManyToMany (trabajadores), prefetch_related.

9. Citas de una Estación	
    Filtra las citas de una estación por cliente y tipo de inspección.	
    Dos parámetros, filtro AND, ManyToOne, select_related.
    
10. Vehículos sin Trabajadores	
    Lista vehículos que no tienen trabajadores asociados.	
    Filtro con None, ManyToMany, filter.


TEMPLATES MEJORADOS y STATICS

    -Primero voy a crear la estructura que la voy a dividir en un padre, en un menu (head) y un footer. Voy a utilizar la misma estructura de la tarea anterior para facilitarme el trabajo

    -Vamos a unificar los templates para no tener dos templates mostrando lo mismo aunque usen views distintas

    -Una vez unificados los he renombrado a listar_loquelisten

    -Vamos a borrar la estructura html de los templates para que extiendan del padre

    -Refactorizamos el contenido creando un html para cada tido de listado ej:vehiculo.html,trabajador.html etc...

    -Voy a realizar un bloque de ifs else, para el "tipo de inspeccion" del modelo cita en el template cita.html, dependiendo de que tipo de cita sea, se coloreara de un color u otro
    
    -Se le da formato todas las fechas

    -Voy aplicar los 10 template filters en el template de vehiculo

        Filtros aplicados:
            -|date:"d/m/Y"
            -|lower
            -|upper
            -|truncatechars:10
            -|length (Cuento el numero de trabajadores que hay en la lista)
            -|default:"Sin notas"
            -inspección{{ vehiculo.vehiculo_Inspeccion.all|pluralize:"es" }} 
            -|add:"2"
            -|divisibleby:"2"
            -|get_digit:"1"


## Widgets utilizados en los formularios del proyecto

- **forms.SelectDateWidget**: Usado para seleccionar fechas en varios formularios.
- **forms.TextInput**: Usado para campos de texto simples.
- **forms.DateInput**: Configurado con el atributo `type="date"` para entrada de fechas.
- **forms.CheckboxInput**: Usado para seleccionar opciones booleanas.
- **forms.Select**: Usado para desplegables con una sola selección.
- **forms.SelectMultiple**: Usado para desplegables con selección múltiple.
- **forms.NumberInput**: Usado para entradas de números.



## Validaciones utilizadas en los formularios del proyecto

### ClienteForm
- **DNI**:
  - Debe cumplir con el patrón: `^[0-9]{8}[A-Z]$`.
  - No debe existir previamente en la base de datos.

### BusquedaAvanzadaCliente
- Al menos un campo debe estar relleno (`nombre`, `dni`, o `fecha_nacimiento`).
- **Nombre**:
  - Máximo 50 caracteres.
- **Fecha de nacimiento**:
  - No puede ser una fecha futura.
- **DNI**:
  - Debe cumplir con el patrón: `^[0-9]{8}[A-Z]$`.

### InspeccionForm
- **Fecha de inspección**:
  - No puede ser una fecha futura.
- **Notas de inspección**:
  - No puede estar vacío o contener solo espacios.

### BusquedaAvanzadaInspeccion
- Al menos un campo debe estar relleno (`resultado_inspeccion`, `notas_inspeccion`, o `fecha_inspeccion`).
- **Resultado de inspección**:
  - No puede contener el carácter `_`.
- **Notas de inspección**:
  - No puede contener el carácter `!`.
- **Fecha de inspección**:
  - No puede ser una fecha futura.

### VehiculoForm
- **Tipo de vehículo**:
  - Si es "moto", no puede tener más de un asiento.
  - Si es "bus", debe tener más de dos ejes.
- **Matrícula**:
  - Debe ser única en la base de datos.

### BusquedaAvanzadaVehiculo
- Al menos un campo debe estar relleno (`marca`, `potencia`, o `matrícula`).
- **Marca**:
  - No puede contener el carácter `_`.
- **Potencia**:
  - Debe ser mayor que 0.
- **Matrícula**:
  - No puede contener el carácter `!`.

### LocalForm
- **Precio**:
  - No puede ser negativo.
- **Metros**:
  - No puede ser negativo.

### BusquedaAvanzadaLocal
- Al menos un campo debe estar relleno (`precio`, `metros`, o `anio_arrendamiento`).
- **Precio**:
  - No puede ser negativo.
- **Metros**:
  - No puede ser negativo.
- **Año de arrendamiento**:
  - No puede ser una fecha futura.

### EstacionForm
- **Comunidad Autónoma**:
  - Debe comenzar con una letra mayúscula.
- **Eficiencia Energética**:
  - No puede estar vacío o contener solo espacios.

### BusquedaAvanzadaEstacion
- Al menos un campo debe estar relleno (`nombre`, `munipio`, o `comunidad_autonoma`).
- **Nombre**:
  - Debe comenzar con una letra mayúscula.
- **Municipio**:
  - No puede comenzar con un número.
- **Comunidad Autónoma**:
  - No puede contener el carácter `_`.

### TrabajadorForm
- **Observaciones**:
  - No puede contener el carácter `!`.
- **Sueldo**:
  - No puede ser negativo.

### BusquedaAvanzadaTrabajador
- Al menos un campo debe estar relleno (`nombre`, `sueldo`, o `puesto`).
- **Nombre**:
  - Debe tener al menos 3 caracteres.
  - No puede contener números.
- **Sueldo**:
  - Debe ser mayor que 10.
- **Puesto**:
  - No puede contener caracteres especiales como `@`, `#`, `$`, `%`, `&`, `*`.


INSTALACION PILLOW PARA IMAGENES EN FORMULARIO

    -Crear carpeta media/imagenes en la carpeta raiz del proyecto
    -Añadir Pillow~=11.0.0, en los requirements.txt
    -He añadido el campo imagen en el modelo cliente
    -Al hacer el makemigrations he usado la opcion de añadir por defecto la misma imagen en todos los objetos cliente de mi base de datos
    -Hacemos el migrate
    -Vemos ahora que en nuestros formularios tenemos el campo para subir una imagen y podemos ver la que actualmente tenemos seleccionada.
    -He modificado el template del cliente para que aparezca la imagen con el siguiente bloque de boostrap
        <p class="card-text">
            <strong>Imagen:</strong>
            <img src="{{ cliente.imagen.url }}" class="img-fluid" alt="Imagen de {{ cliente.nombre }}">
        </p>