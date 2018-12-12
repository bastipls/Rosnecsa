from django.contrib import admin
from .models import Tecnico,Cliente,Folio,Empresa_tecnico

admin.site.register(Tecnico)    
admin.site.register(Cliente)
admin.site.register(Folio)
admin.site.register(Empresa_tecnico)