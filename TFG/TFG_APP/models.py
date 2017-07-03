from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

DEFAULT_USER_ID = 1

class Resultado(models.Model):    
    sujeto = models.ForeignKey(User, on_delete=models.CASCADE, default=DEFAULT_USER_ID)    
    id_sujeto = models.IntegerField(default=0)
    nombre_sujeto = models.CharField(max_length=100, default="nombre sujeto")    
    fecha = models.DateTimeField('date created', default=timezone.now)      
    es_evaluacion = models.BooleanField(default=False)
    tiempo_empleado = models.DecimalField(default=0, max_digits=6, decimal_places=1)
    porcentaje_acierto = models.IntegerField(default=0)
    porcentaje_contestado = models.IntegerField(default=0)
    ponderacion = models.DecimalField(default=0, max_digits=6, decimal_places=1)
            
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
    evaluar = models.BooleanField(default=False)
    numero_sesiones = models.IntegerField(default=3)
    sesiones_completadas = models.IntegerField(default=0)
    tiempo_minimo_entre_sesiones = models.IntegerField(default=12)
    numero_items_por_sesion = models.IntegerField(default=10)
    tiempo_entre_items = models.IntegerField(default=3)
    tiempo_limite_item = models.IntegerField(default=3)    
    magnitud_item = models.CharField(max_length=100, default="normal")
    rendimiento = models.CharField(max_length=50, default="normal")
    ponderacion = models.DecimalField(default=0, max_digits=6, decimal_places=1)
    usar_tareas_apoyo = models.BooleanField(default=False)
    
    def __str__(self):
        return self.sujeto.username \
               + ',' + str(self.evaluar) \
               + ',' + str(self.numero_sesiones) \
               + ',' + str(self.sesiones_completadas) \
               + ',' + str(self.tiempo_minimo_entre_sesiones) \
               + ',' + str(self.numero_items_por_sesion) \
               + ',' + str(self.tiempo_entre_items) \
               + ',' + str(self.tiempo_limite_item) \
               + ',' + str(self.magnitud_item) \
               + ',' + str(self.usar_tareas_apoyo)
    
       
    
    class Meta(object):
        verbose_name = 'Plan'
        verbose_name_plural = 'Planes'

    
    
