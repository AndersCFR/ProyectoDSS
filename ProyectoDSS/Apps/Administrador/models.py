from django.db import models
# Create your models here.

class Administrador(models.Model):
    idadministrador = models.AutoField(primary_key=True)
    nombreadmin = models.CharField(max_length=1024)
    passwordadmin = models.CharField(max_length=1024)

    #class Meta:
    #    managed = False
    #    db_table = 'administrador'

    empAuth_objects = models.Manager()

class Proyecto(models.Model):
    idproyecto = models.AutoField(primary_key=True)
    idadministrador = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='idadministrador')
    nombresubasta = models.CharField(max_length=1024)
    descripcion = models.CharField(max_length=1024)
    estadoproyecto = models.BooleanField()
    #ganador = models.ForeignKey(Usuario.idusuario, models.DO_NOTHING, db_column='idusuario')

    #class Meta:
    #    managed = False
    #    db_table = 'proyecto'

class Requerimiento(models.Model):
    idrequerimiento = models.AutoField(primary_key=True)
    idproyecto = models.ForeignKey(Proyecto, models.DO_NOTHING, db_column='idproyecto')
    descripcionrequerimiento = models.TextField()  # This field type is a guess.
    presupuestoreferencial = models.DecimalField(max_digits=6, decimal_places=2)

    #class Meta:
    #    managed = False
    #    db_table = 'requerimiento'



