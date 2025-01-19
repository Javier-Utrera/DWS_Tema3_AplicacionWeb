# DWS_Tema3_AplicacionWeb

## Explicación de mi aplicación web

Esta aplicación está enfocada en la gestión del servicio ITV a nivel autonómico. Un cliente, que no necesariamente tiene que ser el dueño del vehículo a inspeccionar, puede pedir una cita en la ITV que desee. Su vehículo será inspeccionado por trabajadores que generarán un resultado de la inspección y su correspondiente factura para el pago.

---

## Modelos, atributos y parámetros

### **Cliente**
Modelo que representa a los clientes de la ITV.

- **Atributos:**
  - `nombre`: CharField (máx. 50 caracteres). Almacena el nombre del cliente.
  - `apellidos`: CharField (opcional, máx. 50 caracteres).
  - `sexo`: CharField con `choices` ('M' o 'F').
  - `fecha_nacimiento`: DateField.
  - `codigo_postal`: IntegerField.
  - `domicilio`: TextField.
  - `correo`: EmailField con validación automática.
  - `telefono`: PositiveIntegerField.
  - `dni`: CharField único (9 caracteres).
  - `dueño`: CharField (50 caracteres), almacena el dueño del local.

---

### **Local**
Modelo que representa los locales donde se pueden establecer estaciones ITV.

- **Atributos:**
  - `precio`: FloatField. Precio del alquiler.
  - `metros`: DecimalField (máx. 50 dígitos, 3 decimales).
  - `anio_arrendamiento`: DateField.

---

### **EstacionItv**
Modelo de las estaciones ITV.

- **Relaciones:**
  - `id_local`: Relación OneToOne con el modelo `Local`.

- **Atributos:**
  - `nombre`: CharField único (50 caracteres).
  - `municipio`: CharField (50 caracteres).
  - `eficiencia_energetica`: CharField (1 carácter, como A, B, C...).
  - `comunidad_autonoma`: CharField.

---

### **Cita**
Modelo que representa las citas para la inspección de vehículos.

- **Relaciones:**
  - `id_cliente`: ForeignKey a `Cliente`.
  - `id_estacion`: ForeignKey a `EstacionItv`.

- **Atributos:**
  - `matricula`: CharField (7 caracteres).
  - `fecha_matriculacion`: DateField.
  - `numero_bastidor`: CharField (17 caracteres).
  - `tipo_inspeccion`: CharField con `choices` (ej.: 'PE', 'NOPE', 'VETAX').
  - `remolque`: BooleanField (por defecto `False`).
  - `tipo_pago`: CharField (`choices`: tarjeta o efectivo).
  - `fecha_propuesta`: DateField.
  - `hora_propuesta`: TimeField.

---

### **EmpresaExterna**
Modelo que representa las empresas externas que mantienen las máquinas de la ITV.

- **Atributos:**
  - `nombre`: CharField.
  - `municipio`: CharField.
  - `coste`: FloatField (editable).
  - `cif`: CharField.

---

### **Maquinaria**
Modelo que representa la maquinaria usada en estaciones ITV.

- **Relaciones:**
  - `id_estacionItv`: ForeignKey a `EstacionItv`.
  - `id_empresaExterna`: OneToOneField a `EmpresaExterna`.

- **Atributos:**
  - `nombre`: CharField.
  - `tipo`: CharField (`choices`: emisiones, frenos, dirección).
  - `ultimo_mantenimiento`: DateField (opcional).
  - `funcionando`: BooleanField (por defecto `True`).

---

### **Trabajador**
Modelo que representa a los trabajadores de las estaciones ITV.

- **Relaciones:**
  - `id_estacion`: ManyToManyField con `EstacionItv`.
  - `jefe`: ManyToManyField recursivo (`self`).

- **Atributos:**
  - `nombre`: CharField.
  - `apellidos`: CharField.
  - `puesto`: CharField con `choices`.
  - `sueldo`: FloatField.
  - `observaciones`: TextField.

---

### **Vehiculo**
Modelo que representa los vehículos inspeccionados.

- **Relaciones:**
  - `trabajadores`: ManyToManyField con `Trabajador` (a través de `Inspeccion`).

- **Atributos:**
  - `fecha_matriculacion`: DateField.
  - `marca`, `modelo`, `numero_bastidor`: CharField.
  - `tipo_vehiculo`: CharField (`choices`).
  - `cilindrada`, `potencia`: IntegerField.
  - `combustible`: CharField (`choices`: gasolina, diésel, eléctrico...).
  - `mma`: PositiveIntegerField.
  - `asientos`, `ejes`: PositiveSmallIntegerField.
  - `dni_propietario`, `matricula`: CharField.

---

### **Inspeccion**
Modelo que representa las inspecciones realizadas.

- **Relaciones:**
  - `trabajador`: ForeignKey a `Trabajador`.
  - `vehiculo`: ForeignKey a `Vehiculo`.

- **Atributos:**
  - `fecha_inspeccion`: DateField (por defecto `timezone.now`).
  - `resultado_inspeccion`, `notas_inspeccion`: CharField y TextField.
  - `cliente_puntual`: BooleanField (por defecto `True`).

---

### **Factura**
Modelo que representa las facturas generadas.

- **Relaciones:**
  - `id_inspeccion`: OneToOneField con `Inspeccion`.

- **Atributos:**
  - `importe`: DecimalField.
  - `pagado`: BooleanField.
  - `fecha_emision_factura`: DateField.
  - `observaciones`: TextField.

---

## Vistas

1. **Lista de Clientes**: Ordenados por sexo, nombre y fecha de nacimiento.
2. **Citas de un Cliente**: Muestra citas asociadas a un cliente.
3. **Estaciones con Locales**: Lista estaciones y sus locales.
4. **Trabajadores de Estación**: Muestra trabajadores de una estación.
5. **Inspecciones de Vehículo**: Lista inspecciones de un vehículo por matrícula.
6. **Maquinaria y Empresa**: Detalle de maquinaria y su empresa asociada.
7. **Citas por Rango de Fechas**: Cita más reciente en un rango de años.
8. **Conteo de Vehículos**: Cuenta vehículos por combustible.
9. **Citas de una Estación**: Filtra citas por cliente y tipo.
10. **Vehículos sin Trabajadores**: Lista vehículos sin trabajadores.

---

## Widgets en Formularios

- `forms.SelectDateWidget`
- `forms.TextInput`
- `forms.DateInput`
- `forms.CheckboxInput`
- `forms.Select`
- `forms.SelectMultiple`
- `forms.NumberInput`

---

## Validaciones en Formularios

Se incluyen validaciones específicas para campos como DNI, fechas, resultados y relaciones.

---

## Instalación de Pillow para manejo de imágenes

1. Crear carpeta `media/imagenes` en la raíz del proyecto.
2. Agregar `Pillow~=11.0.0` al archivo `requirements.txt`.
3. Configurar modelos y formularios para admitir campos de imágenes.


# Funcionalidades Nuevas Implementadas TEMA 7 PERMISOS
Datos. He tenido que crear un crud nuevo para el usuario "cliente" , en la anterior entrega no habia tenido en cuenta que casi todo lo que se podia crear con mis cruds era para el administrador

El usuario cliente puede usar los crud de Citas y Vehiculo
El usuario trabajador puede usar el crud de Inspeccion


## 1. Tipos de Usuarios Claramente Diferenciados  
He creado un nuevo model 'Usuario' donde he detallado ademas del usuario Administrador, dos usuarios mas, el "Cliente" y el "Trabajador" 

      ROLES = (
        (ADMINISTRADOR,"administrador"),
        (CLIENTE,"cliente"),
        (TRABAJADOR,"trabajador")
    )

## 2. Control de Permisos y Autenticación en Vistas  
En cada vista, se ha implementado el control de permisos para verificar si el usuario está logueado o no, y si tiene permisos para acceder a esa vista.  
Aunque hay crud donde mis usuarios no pueden acceder, les he asignados permisos de todas formas.

    @permission_required('ITV.add_cita') 

## 3. Control de Permisos en Plantillas  
En cada template (vista y formulario), se ha controlado si el usuario está logueado y si tiene permisos para acceder o interactuar con los formularios y las vistas.  
En el template de menu.html he controlado que bloques de urls estan accesibles para los distintos tipos de usuarios

    {% if request.user.is_authenticated and perms.ITV.add_cita%}

## 4. Variables Guardadas en la Sesión  
Se han incluido al menos cuatro variables que se guardan en la sesión y que aparecen siempre en la cabecera de la página. Estas variables se eliminan cuando el usuario se desloguea.  
En en la funcion index he creado 4 variabless para mostrarlas en el template de menu.html. En esta funcion compruebo so existen dichas variables cuando el usuario entra en mi pagina web.

He controlado que si el usuario de la sesion no pertenece a mi aplicacion con request.user.is_anonymous, solo va crear la fecha de inicio de sesion, en caso que si pertenezca a mi aplicacion se crearan las demas variables

El metodo que usas para borrar los datos de la sesion no consigo ver como lo implementes, con el depurador he manjeado la informacion del request, y al usar el logout las variables son elminadas de la sesion.


## 5. Registro de Usuarios y Validaciones  
Se ha implementado un sistema de registro para los distintos tipos de usuario (excepto el administrador). Este sistema incluye validaciones específicas para controlar que, dependiendo del tipo de usuario, se asignen valores correspondientes.  
He controlado que al registrar segun el tipo de usuario que vamos a registrar, primero lo añada al grupo correspondiente y luego lo cree si no hay errores en las validaciones.

Para mostrar y ocultar los campos he usado el script de campos.js. Me ha costado un par de vueltas que en caso de que el usuario al registrarse tenga algun error de validacion y la pagina se vuelva a ocultar, los campos mostrados y ocultados sean los mismos

## 6. Login y Logout de Usuario  
Se ha implementado un sistema de login y logout para los usuarios.  
Hemos usado el sistema de loging y logout que nos proporciona el propio django incluyengo en urls.py dentro de mysite 
  path('accounts/', include('django.contrib.auth.urls'))
Se ha tenido en cuenta la configuracion en el settings.py,ademas de crear el template de login.html y controlar que si un usuario esta logueado, no le aparezca el boton de login, que le salga el boton de logout

## 7. Variación de Contenido en Formularios Según el Usuario Logueado  
En algún formulario, se ha creado una funcionalidad que hace que el contenido de algún campo `ManyToMany` o `ManyToOne` varie dependiendo del usuario logueado.

Esta funcionalidad la he implementado cuando un trabajador crea una inspeccion, en mi aplicacion un trabajador puede trabajar en varias estaciones de itv a la vez, he pensado que seria buena idea hacer que un trabajador solo pueda realizar inspecciones de los vehiculos que esten en las estaciones donde el trabaja.

Para ello he usado un formulario de inspeccion ModelForm pero usando el request para crear un field que no importo automaticamente del modelo

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(InspeccionForm, self).__init__(*args, **kwargs)
          --Aqui busco el trabajador de mi sesion activa
        trabajador = Trabajador.objects.get(id=self.request.user.trabajador.id)
          --Busco todas las estaciones donde este trabajador se encuentre prestando servicio
        estaciones = trabajador.estacion.all()
          --Filtro los vehiculos que se encuentran en las estaciones buscadas anteriormente
        vehiculos_disponibles = Vehiculo.objects.filter(trabajadores__estacion__in=estaciones).distinct()
          --Aqui creo el campo vehiculo con los resultados de la busqueda
        self.fields["vehiculo"] = forms.ModelChoiceField(
            queryset=vehiculos_disponibles,
            widget=forms.Select,
            required=True,
            empty_label="Seleccione un vehículo"
        )

## 8. Registro de Usuario en Formularios de Creación  
En los formularios de creación, se incluye siempre el usuario que crea el registro a través de la sesión del usuario.  

