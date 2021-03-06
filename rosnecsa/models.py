from django.db import models
from django.utils import timezone



class Cliente (models.Model):
    id_cliente = models.AutoField(primary_key=True)#Y29waW9u 
    nombre_cliente = models.CharField(max_length=30,null=False,blank=True)
    apellidos_cliente = models.CharField(max_length=30,null=True,blank=True)
    comuna_cliente = models.CharField(max_length=30)        
    telefono_cliente = models.IntegerField(blank=True,null=True)
    correo_cliente = models.EmailField(max_length=30)

    def __str__(self):
        return self.nombre_cliente 

class Tecnico (models.Model):
    
    rut_tecnico = models.CharField(primary_key=True,max_length=10)
    email_tecnico = models.EmailField(null=False,blank=True,max_length=30)
    nombre_tecnico = models.CharField(null=False,blank=False ,max_length=30)
    apellido_tecnico = models.CharField(null=False,blank=True,max_length=30)
    cliente = models.ManyToManyField( Cliente,blank=True)

    def __str__(self):
        return self.rut_tecnico


class Folio(models.Model):
    n_folio = models.AutoField(primary_key = True)
    cliente_folio = models.ForeignKey(Cliente,blank=False,null=False,on_delete=models.CASCADE)
    fecha_folio = models.DateField(default=timezone.now ,blank=False,null=True)#Y29waW9u 
    hora_inicio_folio = models.TimeField(default=timezone.now , blank=False,null=False)
    hora_termino_folio = models.TimeField(blank= False,null=False)
    codigo_ascensor = models.CharField(max_length=30,blank=False,null=False)
    fallas_detectadas_folio = models.TextField(max_length=150,blank=False,null=True)
    reparaciones_efectuadas_folio = models.TextField(max_length=150,blank=True,null=True)
    piezas_cambiadas_folio = models.TextField(max_length=150,blank=True,null=True)
    receptor_trabajo_folio = models.ForeignKey(Tecnico, blank=False,null=False,on_delete=models.CASCADE)

    def __int__(self):
        return self.n_folio

class Empresa_tecnico (models.Model):
    email_empleado = models.EmailField(max_length=30)

    def __str__(self):
        return self.email_empleado#Y29waW9u 