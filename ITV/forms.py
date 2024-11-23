from django import forms
from django.forms import ModelForm
from .models import *
from datetime import *
import re 

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
        
        nombre=self.cleaned_data.get('nombre')
        apellidos=self.cleaned_data.get('apellidos')
        sexo=self.cleaned_data.get('sexo')
        fecha_nacimiento=self.cleaned_data.get('fecha_nacimiento')
        codigo_postal=self.cleaned_data.get('codigo_postal')
        domicilio=self.cleaned_data.get('domicilio')
        correo= self.cleaned_data.get('correo')
        telefono=self.cleaned_data.get('telefono')
        dni=self.cleaned_data.get('dni')
        
        #VALIDAMOS DNI
        
        expresion = "^[0-9]{8}[A-Z]$"
        
        if(not re.search(expresion,dni)):
            self.add_error("dni","El formato del dni no es correcto")
        
        dniCliente=Cliente.objects.filter(dni=dni).first()
        
        if(dniCliente):
           self.add_error("dni","El dni ya existe en la base de datos") 
           
        return self.cleaned_data
    
    
class InspeccionForm(ModelForm):
    class Meta:
        model=Inspeccion
        fields=["fecha_inspeccion","resultado_inspeccion","notas_inspeccion",
                "cliente_puntual","trabajador","vehiculo"]
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
        }
    
    def clean(self):
        
        super().clean()
        
        trabajador = self.cleaned_data.get('trabajador') 
        vehiculo = self.cleaned_data.get('vehiculo') 
        fecha_inspeccion =self.cleaned_data.get('fecha_inspeccion') 
        resultado_inspeccion = self.cleaned_data.get('resultado_inspeccion') 
        notas_inspeccion = self.cleaned_data.get('notas_inspeccion') 
        cliente_puntual= self.cleaned_data.get('cliente_puntual') 
        #Que la fecha de inspeccion no puede superior a la actual
            
        return self.cleaned_data