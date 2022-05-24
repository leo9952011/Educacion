from tkinter import Widget
from django import forms
from django.forms import ModelForm

from .models import Persona

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = ['dni','nombrePersona','apellidoPersona','fechaNac','email','tel', 'ciudad']
        labels = {
            'dni': 'DNI',
            'nombrePersona': 'Nombre completo',
            'apellidoPersona': 'Apellido',
            'fechaNac': 'Fecha de Nacimiento',
            'tel': 'Telefono',
            'ciudad': 'Ciudad'
        }
        widgets = {
            'dni': forms.NumberInput(),
            'apellidoPersona':forms.TextInput(),
            'fechaNac':forms.DateInput,
            'tel':forms.NumberInput(),
            'ciudad':forms.Select()
        }

