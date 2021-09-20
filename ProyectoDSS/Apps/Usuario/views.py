from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from ..Administrador.models import Proyecto, Requerimiento
from .models import Puja
import hashlib
import Pyfhel
# Django Encrypt
from .models import Adjudicaciones
from .models import Usuario as Users
from ..Administrador.models import Administrador

from cryptography.fernet import Fernet
import base64
import logging
import traceback
from django.conf import settings



def hash(a):
    encrypt = hashlib.sha256(a.encode('utf-8'))
    return encrypt.digest()

def encrypt(txt):
    try:
        # convert integer etc to string first
        txt = str(txt)
        # get the key from settings
        cipher_suite = Fernet(settings.ENCRYPT_KEY) # key should be byte
        # #input should be byte, so convert the text to byte
        encrypted_text = cipher_suite.encrypt(txt.encode('ascii'))
        # encode to urlsafe base64 format
        encrypted_text = base64.urlsafe_b64encode(encrypted_text).decode("ascii")
        return encrypted_text
    except Exception as e:
        # log the error if any
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None




# Create your views here.
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'registration/login.html')

#@login_required()
def pujar(request):
    proyectos = Proyecto.objects.all()
    nombreProyecto = proyectos.get().nombresubasta
    descripcion = proyectos.get().descripcion
    requerimientos = Requerimiento.objects.all()
    print(requerimientos)
    context = {'proyectos': nombreProyecto, 'descripcion': descripcion, 'requerimientos':requerimientos}
    return render(request, 'U_pujar_subasta.html', context)

def ofertar(request):
    if request.method == 'POST':
        puja1 = request.POST.get('puja+1')
        puja2 = request.POST.get('puja+2')
        pujas=[puja1, puja2]
        usuarios = Users.objects.all()
        proyectos = Proyecto.objects.all()
        nombreProyecto = proyectos.get().nombresubasta
        descripcion = proyectos.get().descripcion
        requerimientos = Requerimiento.objects.all()
        print(requerimientos)
        context = {'proyectos': nombreProyecto, 'descripcion': descripcion, 'requerimientos':requerimientos}

        for i in range(len(requerimientos)):
            if float(pujas[i]) < requerimientos[i].presupuestoreferencial/2:
                return render(request, 'Advertencia.html', context)
            else:
                pass

        for i in range(len(requerimientos)):
            PujaObject = Puja()
            PujaObject.idrequerimiento=requerimientos[i]
            PujaObject.idusuario=usuarios[1]
            PujaObject.valorpuja=encrypt(pujas[i])
            PujaObject.save()

        return render(request, 'U_pujar_subasta2.html', context)
    else:
        print("Error en peticion")


#@login_required()
def usuarioSubastas(request):
    query_results = Proyecto.objects.all()
    usuarios = Users.objects.all()
    nombreProyecto = query_results.get().nombresubasta
    try:
        adjudicaciones = Adjudicaciones.objects.all()
    except:
       pass

    adjudicacion = 'No'
    estado = 'Finalizado'

    print(usuarios)
    if adjudicaciones is not None:
        for adj in adjudicaciones:
            for user in usuarios:
                if adjudicaciones.get(adj).nombreUsuarioGanador == user.get(user).nombreusuario:
                    print(user.get(user).nombreusuario)
                    print(adjudicacion.get(adj).nombreUsuarioGanador)
                    adjudicacion = 'Si'

    if query_results.get().estadoproyecto == False:
        estado = "En Curso"

    # Creating a dictionary to pass as an argument
    context = {'proyectos': nombreProyecto, 'adjudicacion': adjudicacion, 'estado': estado}
    return render(request, 'U_subastas_disponibles.html', context)

def user_login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = hash(request.POST.get('password'))
        print("Contraseña hash",password)

        rol = request.POST.get('rol')
        print('VALORES DE PETICION')
        print(request.POST.get('username'))
        print(request.POST.get('password'))
        print(request.POST.get('rol'))
        if rol =="user":
            try:
                user = Users.objects.get(nombreusuario=username,passwordusuario=password)
                if user is not None:
                    print("Logueado!!")
                    query_results = Proyecto.objects.all()
                    usuarios = Users.objects.all()
                    nombreProyecto = query_results.get().nombresubasta
                    try:
                        adjudicaciones = Adjudicaciones.objects.all()
                    except:
                        pass

                    adjudicacion = 'No'
                    estado = 'Finalizado'

                    print(usuarios)
                    if adjudicaciones is not None:
                        estado = "Finalizado"
                        print("Por aca")
                        for adj in adjudicaciones:
                            #for user in usuarios:
                            print(adjudicaciones.get().nombreUsuarioGanador.nombreusuario)
                            print(username)
                            if adjudicaciones.get().nombreUsuarioGanador.nombreusuario == username:
                                print(adjudicaciones.get().nombreUsuarioGanador.nombreusuario)
                                print(username)
                                #if adjudicaciones.get(adj).nombreUsuarioGanador == user.get(user).nombreusuario:
                                adjudicacion = 'Si'

                    #if query_results.get().estadoproyecto == False:
                    #    estado = "En Curso"

                    # Creating a dictionary to pass as an argument
                    context = {'proyectos': nombreProyecto, 'adjudicacion': adjudicacion, 'estado': estado}
                    return render(request, 'U_subastas_disponibles.html', context)
                else:
                    print("Usuario no registrado")
                    return render(request, 'registration/login.html')
            except Exception as ex:
                return render(request, 'registration/login.html')
                print(ex)
        elif rol== "admin":
            try:
                user = Administrador.empAuth_objects.get(nombreadmin=username,passwordadmin=password)
                if user is not None:
                    print('Administrador registrado !!!!!!')
                    return render(request, 'A_crear_ver_subasta.html')
                else:
                    print("Usuario no registrado")
                    return render(request, 'registration/login.html')
            except Exception as ex:
                return render(request, 'registration/login.html')
                print(ex)
        else:
            print("Error en la solicitud")
