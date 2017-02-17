from django.contrib import admin
from .models import Resultado, EvaluadoresSujetos

class EvaluadoresSujetosAdmin(admin.ModelAdmin):
    list_display = ('nombre_evaluador', 'nombre_sujeto')

class ResultadosAdmin(admin.ModelAdmin):
    list_display = ('nombre_sujeto', 'fecha', 'evaluacion', 'resultados')
    
admin.site.register(Resultado, ResultadosAdmin)
admin.site.register(EvaluadoresSujetos, EvaluadoresSujetosAdmin)
