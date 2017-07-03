from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.shortcuts import render
from TFG_APP.models import Resultado, EvaluadoresSujetos, Plan
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import Group

# con el modo_debug, se fuerza a crear un plan
# de intervencion de 2 sesiones y 5 items

# direccion del servidor local => http://127.0.0.1:8000
# direccion del servidor real => http://venus-iv8wr84q.cloudapp.net:8000
server_url = 'http://venus-iv8wr84q.cloudapp.net:8000'



# nueva funcion para la interfaz profesional-tutor
def nueva_interfaz(request):
    # obtenemos el usuario desde el request
    usuario = request.user
    # si el usuario tiene el rol 'evaluador' entonces
    # usamos la interfaz de evaluadores. En caso contrario
    # utilizamos la de tutores
    if usuario.groups.filter(name='Evaluador').exists():
        return render(request, 'interfaz.html', {'server_url':server_url})
    else:
        Resultado.objects.order_by("fecha") # se usa - para orden inverso
        resultados = Resultado.objects.filter(sujeto=request.user)
        return render(request, 'interfaz-tutor.html',
                      {'resultados': resultados,
                       'sujeto': request.user.first_name,
                       'server_url':server_url})




# listar los resultados del sujeto en la interfaz de tutor
@login_required
def listar_resultados_tutor(request):
    # buscamos los resultados de ese sujeto y los recuperamos ordenados
    try:
        Resultado.objects.order_by("fecha") # se usa - para orden inverseo
        resultados = Resultado.objects.filter(sujeto=request.user)
        return render(request, 'resultados.html',
                      {'resultados': resultados,
                       'sujeto': request.user.first_name,
                       'server_url':server_url}
                      )
    except ObjectDoesNotExist:
        return render(request, 'error.html', {'error':"No hay resultados"})
    


# mostrar en la interfaz el plan del alumno
@login_required
def ver_plan(request):
    # obtenemos los parametros desde la URL
    identificador = request.GET['id']
       
     # obtenemos el user por el nombre
    try:
        id_usuario = int(identificador)
    except ValueError:
        return render(request, 'error.html', {'error': "id mal parseado"})
    
    # obtenemos la instancia del sujeto por su ID
    try:
        sujeto = User.objects.get(id=id_usuario)
    except ObjectDoesNotExist:
        return render(request, 'error.html', {'error': "id no existe en la base de datos"})

    # recuperamos el plan del usuario
    try:
        plan = Plan.objects.get(sujeto=sujeto.id)
    except ObjectDoesNotExist:
        return render(request, 'error.html', {'error': "no hay plan para este usuario"})

    # devolvemos como respuesta la pagina
    return render(request, 'plan.html',
                      {'plan': plan,
                       'sujeto': sujeto.first_name,
                       'server_url':server_url}
                      )
    

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

    # buscamos los resultados de ese sujeto y los recuperamos
    # ordenados
    try:
        Resultado.objects.order_by("fecha") # se usa - para orden inverseo
        resultados = Resultado.objects.filter(sujeto=sujeto_evaluado)
        return render(request, 'resultados.html',
                      {'resultados': resultados,
                       'sujeto': sujeto_evaluado.first_name,
                       'server_url':server_url}
                      )
    except ObjectDoesNotExist:
        return render(request, 'error.html', {'error':"No hay resultados"})



    
# enviar un plan al cliente cuando lo solicita
def enviar_plan(request):
    # obtenemos los parametros desde la URL
    nombre = request.GET['nombre']
    clave = request.GET['password']    
    # hacemos login en la plataforma con esta informacion
    usuario = authenticate(username=nombre,  password=clave)    
    if usuario is not None:
        if usuario.is_active:
            login(request, usuario)
            # recuperamos el plan del usuario
            plan = Plan.objects.get(sujeto=usuario.id)            
            # enviamos el plan al cliente como respuesta            
            return HttpResponse(str(plan))            
    else:
        return HttpResponse("no se puede autenticar usuario")





# comprueba si son validos los datos de login
# pasados como parametros y devuelve un error o el usuario
def comprobar_login(nombre, clave):
    usuario = authenticate(username=nombre,  password=clave)    
    if usuario is not None:
        if usuario.is_active:
            return usuario
    else:
        return HttpResponse("no se puede autenticar usuario")

        
    


# recibir un resultado por un sujeto
def recibir_resultado(request):
  
    # obtenemos los parametros desde la ULR
    nombre = request.GET['nombre']
    clave = request.GET['password']
    parametro_evaluacion = request.GET['es_evaluacion']    
    porcentaje_acierto = request.GET['porcentaje_acierto']
    porcentaje_contestado = request.GET['porcentaje_contestado']
    # el tiempo es el tiempo medio usado por item
    # durante la intervencion
    tiempo_empleado = request.GET['tiempo_empleado']
    
    # convertimos la string del parametro en un boolean
    es_evaluacion = False;    
    if parametro_evaluacion == 'True' or parametro_evaluacion == 'true':
        es_evaluacion = True
    
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
                es_evaluacion=es_evaluacion,
                tiempo_empleado=tiempo_empleado,
                porcentaje_acierto=porcentaje_acierto,
                porcentaje_contestado=porcentaje_contestado
            )         
          

            # recuperamos el plan del usuario
            plan = Plan.objects.get(sujeto=usuario.id)

            # calculamos la puntuacion ponderada del sujeto
            puntuacion = float(objeto_resultado.porcentaje_acierto) * 0.8 \
            + float(objeto_resultado.porcentaje_contestado) * 0.2
            plan.ponderacion = puntuacion

            # introducimos tambien en el resultado la
            # puntuacion que acabamos de calcular
            objeto_resultado.ponderacion = puntuacion

            # salvamos el objeto en la base de datos
            objeto_resultado.save()

            # vemos si el resultado enviado corresponde a una evaluacion.
            # si se trata de una evaluacion habra que actualizar el plan
            # para que este basado en los resultados de la evaluacion
                        
            if es_evaluacion :

                              
                if puntuacion >= 85:
                    
                    # nivel de rendimiento alto
                    plan.rendimiento = "alto"
                    plan.numero_sesiones = 3
                    plan.numero_items_por_sesion = 15                    
                    plan.magnitud_item = "alta"
                    plan.tiempo_entre_items = 2
                    plan.tiempo_limite_item = 2
                    plan.usar_tareas_apoyo = False;
                    
                elif puntuacion >= 60 and puntuacion < 85:
                    
                    # nivel de rendimiento medio
                    plan.rendimiento = "normal"
                    plan.numero_sesiones = 6
                    plan.numero_items_por_sesion = 20
                    plan.magnitud_item = "alta"
                    plan.tiempo_entre_items = 3
                    plan.tiempo_limite_item = 3
                    plan.usar_tareas_apoyo = False;
                    
                else:
                    
                    # nivel de rendimiento bajo < 60
                    plan.rendimiento = "bajo"
                    plan.numero_sesiones = 7
                    plan.numero_items_por_sesion = 25
                    plan.magnitud_item = "baja"
                    plan.tiempo_entre_items = 3
                    plan.tiempo_limite_item = 4
                    plan.usar_tareas_apoyo = True;

                              
                # actualizamos el resto del plan 
                plan.sesiones_completadas = 0                
                plan.evaluar = False
                
                # el modo debug crea planes mas breves
                modo_debug = True
                if modo_debug :
                    plan.numero_sesiones = 2
                    plan.numero_items_por_sesion = 5
                
            else:
                # si no es una evaluacion incrementamos el numero de sesiones
                plan.sesiones_completadas += 1
                # comprobamos si el usuario ya ha completado el plan,
                # si lo ha hecho debe ser evaluado 
                if plan.sesiones_completadas >= plan.numero_sesiones:
                    plan.sesiones_completadas = 0
                    plan.evaluar = True
                    
                
            # salvamos el plan en la base de datos
            plan.save()

            # enviamos el plan al cliente como respuesta
            return HttpResponse(str(plan))
            
    else:
        return HttpResponse("no se puede autenticar usuario")
        


    

# listar los sujetos de un evaluador
@login_required
def listar_sujetos(request):
   
    # los sujetos que llevada cada evaluador estan en la relacion
    # Evaluadores-Sujetos
    try:
        registros = EvaluadoresSujetos.objects.filter(usuario_propietario=request.user)                   
        return render(request,
                      'sujetos.html',
                      {'sujetos': registros,
                      'server_url':server_url})
    except ObjectDoesNotExist:
        return render(request,
                      'error.html', {'error': "No tiene asignados sujetos"})        
       




# crear un sujeto
@login_required
def nuevo_sujeto(request):

    # recuperamos los parametros desde la URL, hay que
    # aclarar que nombre hace referencia al nombre de usuario,
    # y nombre_completo al del sujeto 
    nombre = request.GET['nombre']
    clave = request.GET['password']
    nombre_completo = request.GET['nombre-completo']
        
    # comprobamos que el nombre de usuario no existe
    if not User.objects.filter(username=nombre).exists():
    
        # obtenemos el id del usuario evaluador que quiere
        # crear el nuevo sujeto 
        id_evaluador = request.user.id        
        # creamos el registro del nuevo sujeto
        nuevo_sujeto = User.objects.create_user(username=nombre,email='',password=clave)
        nuevo_sujeto.first_name = nombre_completo
        # incluimos el nuevo sujeto en el grupo-rol 'sujeto'
        grupo = Group.objects.get(name='Sujeto')
        grupo.user_set.add(nuevo_sujeto)
        nuevo_sujeto.save()
        # creamos el registro en la relacion de evaluadores-sujetos    
        registro = EvaluadoresSujetos(
            usuario_propietario=request.user, 
            id_sujeto=nuevo_sujeto.id,
            id_evaluador=id_evaluador,
            nombre_sujeto=nombre_completo,
            nombre_evaluador=request.user.username)
        registro.save()

        # a continuacion creamos un plan para este nuevo
        # sujeto. Indicamos que el plan esta completo para
        # que se ejecuta la tarea de evaluacion (esto podria
        # dejar de ser necesario si especificamos por defecto
        # el valor True en el models.py
        plan = Plan(sujeto=nuevo_sujeto)
        plan.evaluar = True
        plan.save()

        

        return render(request, 'interfaz.html',
                      {'server_url':server_url,
                       'mensaje_exito': "Se ha introducido un nuevo usuario correctamente" })        
    else:        
         return render(request, 'interfaz.html',
                      {'server_url':server_url,
                       'mensaje_error': "Se ha producido un error: el usuario ya existe" })      
