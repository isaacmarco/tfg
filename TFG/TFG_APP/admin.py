from django.contrib import admin
from .models import Resultado, EvaluadoresSujetos, Plan

class PlanAdmin(admin.ModelAdmin):
    list_display = ('sujeto', 'rendimiento','ponderacion','evaluar',
                    'numero_sesiones',
                    'sesiones_completadas',
                    'numero_items_por_sesion',
                    'tiempo_entre_items',
                    'tiempo_limite_item',
                    'magnitud_item',
                    'usar_tareas_apoyo')
    
class EvaluadoresSujetosAdmin(admin.ModelAdmin):
    list_display = ('nombre_evaluador', 'nombre_sujeto')

class ResultadosAdmin(admin.ModelAdmin):
    list_display = ('nombre_sujeto', 'fecha',
                    'es_evaluacion',
                    'ponderacion',
                    'porcentaje_contestado',
                    'porcentaje_acierto',
                    'tiempo_empleado')


admin.site.register(Plan, PlanAdmin)    
admin.site.register(Resultado, ResultadosAdmin)
admin.site.register(EvaluadoresSujetos, EvaluadoresSujetosAdmin)
