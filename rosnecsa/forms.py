from django import forms
from .models import Folio,Tecnico
from django.contrib.auth.models import User
class FolioForm (forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        def rut(request):

            if  not request.user.is_superuser:
                tecnico = Tecnico.objects.filter(email_tecnico = request.user.email).values_list("rut_tecnico",flat=True)
                

            elif request.user.is_superuser:

                tecnico = Tecnico.objects.filter(email_tecnico = request.user.email).values_list("rut_tecnico",flat=True)
            return tecnico                 
        # tec = tecnico.values("rut_tecnico")
        self.fields['receptor_trabajo_folio'].widget.attrs.update({'value':rut})
    class Meta:
        model = Folio
        fields = ('n_folio','cliente_folio','fecha_folio','hora_inicio_folio','hora_termino_folio',
                'codigo_ascensor','fallas_detectadas_folio','reparaciones_efectuadas_folio','piezas_cambiadas_folio',
                'receptor_trabajo_folio')

class Tecnico (forms.ModelForm):

    class Meta:
        model = Tecnico
        fields = '__all__'