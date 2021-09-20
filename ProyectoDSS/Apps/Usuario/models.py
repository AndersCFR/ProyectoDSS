from django.db import models
from ..Administrador.models import Requerimiento, Proyecto
from django.conf import settings
from django_cryptography.fields import encrypt
# Create your models here.

class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    nombreusuario = models.CharField(max_length=1024)
    passwordusuario = models.CharField(max_length=1024)
    #empAuth_objects = models.Manager()
    #class Meta:
    #    managed = False
    #    db_table = 'usuario'

class Puja(models.Model):
    idpuja = models.AutoField(primary_key=True)
    idrequerimiento = models.ForeignKey(Requerimiento, models.DO_NOTHING, db_column='idrequerimiento')
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idusuario')
    valorpuja = models.TextField()

    #class Meta:
    #    managed = False
    #    db_table = 'puja'

class Adjudicaciones(models.Model):
    #idAdjudicacion = models.AutoField()
    nombreUsuarioGanador = models.ForeignKey(Usuario, models.DO_NOTHING,db_column='nombreusuario')
    idProyecto = models.ForeignKey(Proyecto, models.DO_NOTHING, db_column='idproyecto')
