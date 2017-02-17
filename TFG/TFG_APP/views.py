from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.shortcuts import render
from TFG_APP.models import Resultado, EvaluadoresSujetos
from django.contrib.auth.decorators import login_required

# @login_required() <- esta clasusula se puede poner en todas las funciones!

# intefaz para los evaluadores
@login_required
def interfaz(request):
    return render(request, 'interfaz.html')

# listar los resultados de un sujeto
@login_required
def listar_resultados(request):

    # obtenemos los parametros desde la URL
    identificador = request.GET['id']

    # obtenemos el user por el nombre
    try:
        id_usuario = int(identificador)
    except ValueError:
        return render(request, 'error.html', {'error': "id mal parseado"})
    
    # obtenemos la instancia del sujeto por su ID
    try:
        sujeto_evaluado = User.objects.get(id=id_usuario)
    except ObjectDoesNotExist:
        return render(request, 'error.html', {'error': "id no existe en la base de datos"})

    # buscamos los resultados de ese sujeto
    try:
        resultados = Resultado.objects.filter(sujeto=sujeto_evaluado)
        return render(request, 'resultados.html', {'resultados': resultados})
    except ObjectDoesNotExist:
        return render(request, 'error.html', {'error':"No hay resultados"})
    

# recibir un resultado por un sujeto
def recibir_resultado(request):

    # obtenemos los parametros desde la ULR
    nombre = request.GET['nombre']
    clave = request.GET['password']
    resultado = request.GET['resultado']
    
    # hacemos login en la plataforma con los datos para
    # ver si la peticion tiene autorizacion para introducir los datos
    usuario = authenticate(username=nombre,  password=clave)
    if usuario is not None:
        if usuario.is_active:
            login(request, usuario)
            # creamos el objeto resultado
            objeto_resultado = Resultado(
                sujeto=usuario,
                nombre_sujeto=nombre,
                id_sujeto=usuario.id,
                resultados=resultado)
            objeto_resultado.save()            
            return render(request, 'exito.html')
    else:        
        return render(request, 'error.html', {'error': "Error de autenticacion"})
    

# listar los sujetos de un evaluador
@login_required
def listar_sujetos(request):
   
    # los sujetos que llevada cada evaluador estan en la relacion
    # Evaluadores-Sujetos
    try:
        registros = EvaluadoresSujetos.objects.filter(usuario_propietario=request.user)                   
        return render(request,
                      'sujetos.html', {'sujetos': registros})
    except ObjectDoesNotExist:
        return render(request,
                      'error.html', {'error': "No tiene asignados sujetos"})        
       
    

# crear un sujeto
@login_required
def nuevo_sujeto(request):

    # recuperamos los parametros desde la URL
    nombre = request.GET['nombre']
    clave = request.GET['password']
    
    # comprobamos que el nombre de usuario no existe
    if not User.objects.filter(username=nombre).exists():
    
        # obtenemos el id del usuario evaluador que quiere
        # crear el nuevo sujeto 
        id_evaluador = request.user.id        
        # creamos el registro del nuevo sujeto
        nuevo_sujeto = User.objects.create_user(username=nombre,email='',password=clave)
        # creamos el registro en la relacion de evaluadores-sujetos    
        registro = EvaluadoresSujetos(
            usuario_propietario=request.user, 
            id_sujeto=nuevo_sujeto.id,
            id_evaluador=id_evaluador,
            nombre_sujeto=nombre,
            nombre_evaluador=request.user.username)
        registro.save()
        
        return render(request, 'informacion.html', {'informacion': "Operacion completada"})

    else:
        
        return render(request, 'error.html', {'error': "El usuario ya existe"})
