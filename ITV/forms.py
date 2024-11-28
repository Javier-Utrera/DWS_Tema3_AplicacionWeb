from django import forms
from django.forms import ModelForm
from .models import *
from datetime import *
import re 
from django.utils import timezone 

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre','apellidos','sexo','fecha_nacimiento','codigo_postal',
                'domicilio','correo','telefono','dni']
        labels = {
            "fecha_nacimiento" : ("Fecha de nacimiento"),
            "codigo_postal": ("Codigo postal")
        }
        help_texts = {
            "nombre" : ("50 caracteres como máximo"),
            "apellidos" : ("50 caracteres como máximo"),
            "correo" : ("50 caracteres como máximo"),
            "dni" : ("9 caracteres como máximo")
        }
        widgets = {
            "fecha_nacimiento" : forms.SelectDateWidget(),
            "domicilio" : forms.TextInput(),
        }
        localized_fields = ["fecha_nacimiento"]
        
    def clean(self):
        
        super().clean()
        dni=self.cleaned_data.get('dni')
        
        #VALIDAMOS DNI
        
        expresion = "^[0-9]{8}[A-Z]$"
        
        if(not re.search(expresion,dni)):
            self.add_error("dni","El formato del dni no es correcto")
        
        dniCliente=Cliente.objects.filter(dni=dni).first()
        
        if(dniCliente):
           self.add_error("dni","El dni ya existe en la base de datos") 
           
        return self.cleaned_data

class BusquedaAvanzadaCliente(forms.Form):
    nombre=forms.CharField(required=False,label="Nombre del usuario")
    dni=forms.CharField(required=False,label="Dni del usuario")
    fecha_nacimiento=forms.DateField(required=False,label="Fecha de nacimiento"
                                     ,widget=forms.DateInput(format="%Y-%m-%d", 
                                                            attrs={"type": "date"},
                                                            )
                                    )
    
    def clean(self):
        super().clean()
        
        nombre=self.cleaned_data.get("nombre")
        dni=self.cleaned_data.get("dni") 
        fecha_nacimiento=self.cleaned_data.get("fecha_nacimiento") 
        
        if(nombre == "" and dni == "" and fecha_nacimiento is None):
            self.add_error("nombre","Debe introducir al menos un valor en un campo del formulario")
            self.add_error("dni","Debe introducir al menos un valor en un campo del formulario")
            self.add_error("fecha_nacimiento","Debe introducir al menos un valor en un campo del formulario")
        else:
            if(nombre!="" and len(nombre)>50):
                self.add_error("nombre","No puede introducir mas de 50 caracteres")
            
            if(not fecha_nacimiento is None and fecha_nacimiento>=timezone.now().date()):
                self.add_error("fecha_nacimiento","La fecha de nacimiento no puede ser mayor a la de hoy")
            
            expresion = "^[0-9]{8}[A-Z]$"       
            if(dni!="" and not re.search(expresion,dni)):
                self.add_error("dni","El formato del dni no es correcto")
                
        return self.cleaned_data
class InspeccionForm(ModelForm):
    class Meta:
        model=Inspeccion
        fields='__all__'
        labels= {
            "fecha_inspeccion" : ("Fecha de la inspección"),
            "resultado_inspeccion" : ("Resultado de la inspección"),
            "notas_inspeccion" : ("Notas de la inspección"),
            "cliente_puntual" : ("¿Es un cliente habitual?"),
            "trabajador" : ("Trabajador a cargo"),
            "vehiculo" : ("Vehiculo inspeccionado"),
        }
        widgets = {
            "fecha_inspeccion" : forms.SelectDateWidget(),
            "notas_inspeccion" : forms.TextInput(),
            "cliente_puntual":forms.CheckboxInput(),
            "trabajador" : forms.Select(),
        }
    
    def clean(self):
        
        super().clean()
        
        fecha_inspeccion =self.cleaned_data.get('fecha_inspeccion') 
        notas_inspeccion = self.cleaned_data.get('notas_inspeccion') 
        
        if(fecha_inspeccion>timezone.now().date()):
            self.add_error("fecha_inspeccion","La fecha de la inspeccion no puede ser superior a la actual")
            
        if(notas_inspeccion==" "):
            self.add_error("notas_inspeccion","Las notas de la inspeccion no pueden estar vacias")
            
        return self.cleaned_data
    
class BusquedaAvanzadaInspeccion(forms.Form):
    
    resultado_inspeccion=forms.CharField(required=False,label="Resultado de la inspeccion")
    notas_inspeccion=forms.CharField(required=False,label="Notas de la inspeccion")
    fecha_inspeccion=forms.DateField(required=False,label="Fecha de la inspeccion",
                                     widget=forms.DateInput(format="%Y-%m-%d", 
                                                            attrs={"type": "date"},))
    
    def clean(self):
        
        super().clean()
        
        resultado_inspeccion=self.cleaned_data.get("resultado_inspeccion")
        notas_inspeccion=self.cleaned_data.get("notas_inspeccion") 
        fecha_inspeccion=self.cleaned_data.get("fecha_inspeccion") 
        
        if(resultado_inspeccion =="" and notas_inspeccion=="" and fecha_inspeccion is None):
            self.add_error("resultado_inspeccion","Debes rellenar algun dato")
            self.add_error("notas_inspeccion","Debes rellenar algun dato")
            self.add_error("fecha_inspeccion","Debes rellenar algun dato")
        else:
            if resultado_inspeccion !="" and ('_' in resultado_inspeccion):
                self.add_error("resultado_inspeccion","Este campo no puede contener una _")
            if notas_inspeccion!="" and ('!' in notas_inspeccion):
                self.add_error("notas_inspeccion","Este campo no permite un caracter '!'")
            if not fecha_inspeccion is None and fecha_inspeccion>timezone.now().date():
                self.add_error("fecha_inspeccion","La fecha de la inspeccion no puede ser superior a la de hoy")
        
        return self.cleaned_data       
    
class VehiculoForm(ModelForm):
    class Meta:
        model=Vehiculo
        fields='__all__'
        labels = {
            "fecha_matriculacion": ("Fecha de matriculación"),
            "marca": ("Marca del vehículo"),
            "modelo": ("Modelo del vehículo"),
            "numero_bastidor": ("Número de bastidor"),
            "tipo_vehiculo": ("Tipo de vehículo (ITV)"),
            "cilindrada": ("Cilindrada (cc)"),
            "potencia": ("Potencia (CV)"),
            "combustible": ("Tipo de combustible"),
            "mma": ("Masa Máxima Autorizada (kg)"),
            "asientos": ("Número de asientos"),
            "ejes": ("Número de ejes"),
            "dni_propietario": ("DNI del propietario"),
            "matricula": ("Matrícula"),
            # "trabajadores" : ("Trabajadores")
        }
        help_texts = {
            # "trabajadores" : ("Manten pulsada la tecla control para seleccionar varios elementos"),
        }
        widgets = {
            "fecha_matriculacion" : forms.SelectDateWidget(),
            # "trabajadores" : forms.SelectMultiple(),
            "tipo_vehiculo" : forms.Select(),
            "combustible" : forms.Select(),
            "numero_bastidor":forms.NumberInput
        }
        localized_fields = ["fecha_matriculacion"]
        
    def clean(self):
        super().clean()
        tipo_vehiculo=self.cleaned_data.get("tipo_vehiculo")
        ejes=self.cleaned_data.get("ejes")
        asientos=self.cleaned_data.get("asientos")
        matricula=self.cleaned_data.get("matricula")
        
        if(tipo_vehiculo=="moto" and asientos>1):
            self.add_error("asientos","Para el tipo de vehiculo Motocicleta solo puedes escoger un asiento")
            
        if(tipo_vehiculo=="bus" and ejes<=2):
            self.add_error("ejes","Revisa el tipo de vehiculo, el que has seleccionado tiene mas de 2 ejes")
            
        matriculaVehiculo=Vehiculo.objects.filter(matricula=matricula).first()
        
        if(matriculaVehiculo):
            self.add_error("matricula","Esta matricula ya esta registrada") 
            
        return self.cleaned_data
        
class LocalForm(ModelForm):
    class Meta:
        model=Local
        fields='__all__'
        labels = {
            "precio": ("Precio del local"),
            "metros": ("Metros del local"),
            "anio_arrendamiento": ("Año en el que se arrendó"),
            "duenio": ("Dueño del local")
        }
        widgets = {
            "anio_arrendamiento" : forms.SelectDateWidget(),
            "metros" : forms.NumberInput,
        }
        localized_fields = ["anio_arrendamiento"]
        
    def clean(self):
        super().clean()
        precio=self.cleaned_data.get("precio")
        metros=self.cleaned_data.get("metros")
        
        if (precio<0):
            self.add_error("precio","El precio no puede ser negativo")
        if(metros<0):
            self.add_error("metros","Los metros no pueden ser negativos")
            
        return self.cleaned_data
    
class EstacionForm(ModelForm):
    class Meta:
        model=EstacionItv
        fields='__all__'
        labels = {
            "nombre": ("Nombre de la estacion"),
            "munipio": ("Municipio de la estacion"),
            "eficiencia_energetica": ("Eficiencia energetica"),
            "comunidad_autonoma": ("Comunidad autonoma"),
            "local": ("Locales"),
        }
        help_texts = {
            "eficiencia_energetica" : ("Una sola letra"),
        }
        widgets = {
            "local" : forms.Select()
        }        
        
    def clean(self):
        comunidad_autonoma=self.cleaned_data.get("comunidad_autonoma")
        eficiencia_energetica=self.cleaned_data.get("eficiencia_energetica")
        
        if(comunidad_autonoma[0].islower()):
            self.add_error("comunidad_autonoma","La primera letra tiene que ser mayuscula")
        
        if(eficiencia_energetica==" "):
            self.add_error("eficiencia_energetica","El unico caracter no puede ser un espacio")
        return self.cleaned_data
            
class TrabajadorForm(ModelForm):
    class Meta:
        model=Trabajador
        fields='__all__'
        labels = {
            "nombre": ("Nombre del trabajador"),
            "apellidos": ("Apellidos del trabajador"),
            "puesto": ("Puesto del trabajador"),
            "sueldo": ("Sueldo del trabajador"),
            "observaciones": ("Observaciones del trabajador"),
            "estacion": ("Estacion del trabajador"),  
        }
        widgets = {
            "estacion" : forms.SelectMultiple()
        }
    
    def clean(self):
        sueldo=self.cleaned_data.get("sueldo")
        observaciones=self.cleaned_data.get("observaciones")
        caracter="!"
        
        if caracter in observaciones:
            self.add_error("observaciones","El campo observaciones no puede contener un '!'")
            
        if sueldo < 0:
            self.add_error("sueldo","El sueldo no puede ser negativo")
            
        return self.cleaned_data
            
        