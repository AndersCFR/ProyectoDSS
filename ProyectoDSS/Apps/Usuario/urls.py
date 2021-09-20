from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('pujar',views.pujar, name='pujar'),
    path('usuarioSubastas',views.usuarioSubastas, name='usuarioSubastas'),
    path('usuarioLogin', views.user_login, name='user_login'),
    path('ofertar', views.ofertar, name='ofertar')
]