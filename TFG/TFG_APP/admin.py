from django.contrib import admin
from .models import Resultado, EvaluadoresSujetos, Plan

class PlanAdmin(admin.ModelAdmin):
    list_display = ('sujeto', 'completado', 'dificultad',
                    'tipo_operaciones', 'numero_sesiones',
                    'sesiones_completadas',
                    'numero_items_por_sesion',
                    'tiempo_minimo_entre_sesiones')
    
class EvaluadoresSujetosAdmin(admin.ModelAdmin):
    list_display = ('nombre_evaluador', 'nombre_sujeto')

class ResultadosAdmin(admin.ModelAdmin):
    list_display = ('nombre_sujeto', 'fecha', 'es_evaluacion', 'porcentaje_acierto', 'tiempo_empleado', 'resultados')


admin.site.register(Plan, PlanAdmin)    
admin.site.register(Resultado, ResultadosAdmin)
admin.site.register(EvaluadoresSujetos, EvaluadoresSujetosAdmin)
