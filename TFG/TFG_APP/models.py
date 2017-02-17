from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

DEFAULT_USER_ID = 1

class Resultado(models.Model):    
    sujeto = models.ForeignKey(User, on_delete=models.CASCADE, default=DEFAULT_USER_ID)    
    id_sujeto = models.IntegerField(default=0)
    nombre_sujeto = models.CharField(max_length=100, default="nombre sujeto")    
    fecha = models.DateTimeField('date created', default=datetime.now)      
    evaluacion = models.BooleanField(default=False)
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
