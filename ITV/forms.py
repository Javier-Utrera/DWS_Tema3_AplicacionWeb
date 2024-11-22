from django import forms
from django.forms import ModelForm
from .models import *
from datetime import *

class CrearCliente(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre','apellidos','sexo','fecha_nacimiento','codigo_postal',
                'domicilio','correo','telefono','dni']
        labels = {
            "fecha_nacimiento" : ("Fecha de nacimiento"),
            "codigo_postal": ("Codigo postal")
        }
        # initial= {"fecha_nacimiento":datetime.date.today,
        #           "sexo":"F"
        # }
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