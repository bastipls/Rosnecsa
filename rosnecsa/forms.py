from django import forms
from .models import Folio,Tecnico,Cliente
from django.contrib.auth.models import User



class FolioForm (forms.ModelForm):#Y29waW9u 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['hora_inicio_folio'].widget.attrs.update({'readonly':'True'})
     

    fecha_folio = forms.DateField(widget=forms.DateInput(format='%H:%M',attrs={'type':'date'}))   
    hora_termino_folio = forms.TimeField(widget=forms.TimeInput(format='%H:%M',attrs={'type':'time'}))
  
    class Meta:
        model = Folio
        
       
        fields = ('n_folio','cliente_folio','fecha_folio','hora_inicio_folio','hora_termino_folio',
                'codigo_ascensor','fallas_detectadas_folio','reparaciones_efectuadas_folio','piezas_cambiadas_folio',
                'receptor_trabajo_folio')
                

class TecnicoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cliente'].widget.attrs.update({'multiple':True})
        self.fields['rut_tecnico'].widget.attrs.update({'required':'True','readonly':'True'})
        
    class Meta:
        model = Tecnico
        fields = ('rut_tecnico','cliente')
class ClienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre_cliente'].widget.attrs.update({'required':'True','placeholder':'Ingrese nombre'})
        self.fields['apellidos_cliente'].widget.attrs.update({'required':'True','placeholder':'Ingrese apellido'})#Y29waW9u 
        self.fields['comuna_cliente'].widget.attrs.update({'required':'True','placeholder':'Ingrese comuna'})
        self.fields['telefono_cliente'].widget.attrs.update({'required':'True','placeholder':'Ingrese telefono'})
        self.fields['correo_cliente'].widget.attrs.update({'required':'True','placeholder':'Ingrese correo'})

    class Meta:
        model = Cliente
        fields = '__all__'        