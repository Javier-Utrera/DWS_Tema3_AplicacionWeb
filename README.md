# DWS_Tema3_AplicacionWeb
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

Modelo: Factura

Este modelo representa las facturas generadas.

    Relaciones:
        id_inspeccion: Relación OneToOneField con Inspeccion, cada inspección genera una factura.
        resultado: Relación OneToOneField con Inspeccion, usando un related_name para diferenciar la relación.

    Atributos:
        importe: Importe de la factura, almacenado como DecimalField para mayor precisión.
        pagado: Campo BooleanField para indicar si se ha pagado la factura.
