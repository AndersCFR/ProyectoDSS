from django.contrib import admin
from .models import Administrador, Proyecto, Requerimiento
# Register your models here.

admin.site.register(Administrador)
admin.site.register(Proyecto)
admin.site.register(Requerimiento)

