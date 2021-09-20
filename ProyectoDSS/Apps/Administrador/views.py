from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import Proyecto, Requerimiento
from ..Usuario.models import Puja, Adjudicaciones, Usuario

from cryptography.fernet import Fernet
import base64
import logging
import traceback
from django.conf import settings

def decrypt(txt):
    try:
        # base64 decode
        txt = base64.urlsafe_b64decode(txt)
        cipher_suite = Fernet(settings.ENCRYPT_KEY)
        decoded_text = cipher_suite.decrypt(txt).decode("ascii")
        return decoded_text
    except Exception as e:
        # log the error
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None


@login_required()
def crearSubasta(request):
    # Getting all the stuff from database
    query_results = Proyecto.objects.all();
    query_results2 = Requerimiento.objects.all();

    # Creating a dictionary to pass as an argument
    context = {'query_results': query_results, 'query_results2': query_results2}
    print(query_results.get().descripcion)
    return render(request, 'A_crear_subasta.html', context)

@login_required()
def menuAdmin(request):
    return render(request, 'A_crear_ver_subasta.html')

#@login_required()
def ganador(request):
    proyecto = Proyecto.objects.all()
    nombreProyecto = proyecto.get().nombresubasta
    descripcion = proyecto.get().descripcion
    query_results2 = Puja.objects.all()
    pujas = query_results2.all()

    participantes = []
    pujasTotales=[]
    for puja in pujas:
        if puja.idusuario not in participantes:
            participantes.append(puja.idusuario)
            #pujasTotales.append(puja)

    for participante in participantes:
        pujaTotal=0
        for puja in pujas:
            if int(puja.idusuario.idusuario) == int(participante.idusuario):
                print("Siii")
                pujaTotal= pujaTotal+float(decrypt(puja.valorpuja))
        pujasTotales.append(pujaTotal)

    for puja in pujasTotales:
        print(puja)

    menorPuja = min(pujasTotales)
    indexUsuarioGanador = pujasTotales.index(menorPuja)

    print(indexUsuarioGanador)

    print(participantes[indexUsuarioGanador].idusuario)
    print(participantes[indexUsuarioGanador].nombreusuario)

    idUsuarioGanador = participantes[indexUsuarioGanador].idusuario
    nombreUsuarioGanador = participantes[indexUsuarioGanador].nombreusuario

    AdjudicacionGanador = Adjudicaciones()
    AdjudicacionGanador.nombreUsuarioGanador=participantes[indexUsuarioGanador]
    AdjudicacionGanador.idProyecto=proyecto.get()
    AdjudicacionGanador.save()

    context = {'nombreProyecto': nombreProyecto, 'descripcion': descripcion, 'ganador': nombreUsuarioGanador}
    return render(request, 'A_ver_ganador.html', context)

#@login_required()
def verSubastas(request):
    query_results = Proyecto.objects.all()
    query_results2 = Puja.objects.all()
    proyectos = query_results.get()
    pujas = query_results2.all()

    participantes = []
    estadoSubasta = 'No asignado'
    nombreProyecto = Proyecto.objects.get().nombresubasta
    for puja in pujas:
        if puja.idusuario not in participantes:
            participantes.append(puja.idusuario)
    numeroParticipantes = len(participantes)

    if proyectos.estadoproyecto == False:
        estadoSubasta = 'En curso'
    else:
        estadoSubasta = 'Finalizada'

    context = {'nombreProyecto': nombreProyecto, 'numeroParticipantes': numeroParticipantes, 'estado': estadoSubasta}
    return render(request, 'A_ver_subastas.html', context)


