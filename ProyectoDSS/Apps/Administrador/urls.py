from django.urls import path
from . import views
urlpatterns = [
    path('administrador', views.menuAdmin, name='menuAdmin'),
    path('ganador', views.ganador, name='ganador'),
    path('listaSubastas',views.verSubastas, name='verSubastas'),
    path('crearSubasta', views.crearSubasta, name='crearSubasta'),
]