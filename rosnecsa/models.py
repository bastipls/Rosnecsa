from django.db import models
from django.utils import timezone


class Tecnico (models.Model):
    
    rut_tecnico = models.CharField(primary_key=True,max_length=10)
    email_tecnico = models.CharField(null=False,blank=True,max_length=30)
    nombre_tecnico = models.CharField(null=False,blank=False,max_length=30)
    apellido_tecnico = models.CharField(null=False,blank=True,max_length=30)

    def __str__(self):
        return self.rut_tecnico