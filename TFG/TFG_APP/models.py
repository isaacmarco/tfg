from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

DEFAULT_USER_ID = 1

class Resultado(models.Model):    
    sujeto = models.ForeignKey(User, on_delete=models.CASCADE, default=DEFAULT_USER_ID)    
    id_sujeto = models.IntegerField(default=0)
    nombre_sujeto = models.CharField(max_length=100, default="nombre sujeto")    
    fecha = models.DateTimeField('date created', default=datetime.now)      
    es_evaluacion = models.BooleanField(default=False)
    tiempo_empleado = models.IntegerField(default=0)
    porcentaje_acierto = models.IntegerField(default=0)
    resultados = models.CharField(max_length=100)
        
    def __unicode__(self):
        return self.nombre_sujeto

    class Meta(object):
        verbose_name = 'Resultado'
        verbose_name_plural = 'Resultados'
    
  
    
class EvaluadoresSujetos(models.Model):    
    usuario_propietario = models.ForeignKey(User, on_delete=models.CASCADE, default=DEFAULT_USER_ID)
    id_evaluador = models.IntegerField(default=0)
    id_sujeto = models.IntegerField(default=0)
    nombre_sujeto = models.CharField(max_length=100, default="nombre sujeto")
    nombre_evaluador = models.CharField(max_length=100, default="nombre evaluador")
     
    class Meta(object):
        verbose_name = 'Evaluador-Sujeto'
        verbose_name_plural = 'Evaluadores-Sujetos'


class Plan(models.Model):
    sujeto = models.ForeignKey(User, on_delete=models.CASCADE, default=DEFAULT_USER_ID)
    completado = models.BooleanField(default=False)
    dificultad = models.CharField(max_length=100, default="facil")
    tipo_operaciones = models.CharField(max_length=100, default="sumas")
    numero_sesiones = models.IntegerField(default=5)
    sesiones_completadas = models.IntegerField(default=0)
    numero_items_por_sesion = models.IntegerField(default=10)
    tiempo_minimo_entre_sesiones = models.IntegerField(default=12)
    
    class Meta(object):
        verbose_name = 'Plan'
        verbose_name_plural = 'Planes'

    
    
