"""TFG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from TFG_APP.views import nuevo_sujeto, listar_sujetos, recibir_resultado,listar_resultados
from TFG_APP.views import nueva_interfaz, enviar_plan, ver_plan

urlpatterns = [    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^interfaz/$', nueva_interfaz),    
    url(r'^nuevo-sujeto/$', nuevo_sujeto),
    url(r'^enviar-plan/$', enviar_plan),
    url(r'^ver-plan/$', ver_plan),
    url(r'^listar-sujetos/$', listar_sujetos),
    url(r'^recibir-resultado/$', recibir_resultado),
    url(r'^listar-resultados/$', listar_resultados),
    url(r'^$', 'django.contrib.auth.views.login')
]
