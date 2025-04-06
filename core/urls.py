from django.urls import path
from . import views

urlpatterns = [
    path('', views.menuprincipal, name='menuprincipal'),  # Ruta raíz como 'menuprincipal'
    path('foro/', views.foro, name='foro'),
    path('micuenta/', views.micuenta, name='micuenta'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('login/', views.login, name='login'),
    path('recuperar/', views.recuperar_contra, name='recuperar'),
    path('lugares/', views.lugares, name='lugares'),
    path('animales/', views.animales, name='animales'),
    path('armas/', views.armas, name='armas'),
    path('construcciones/', views.construcciones, name='construcciones'),
    path('consumibles/', views.consumibles, name='consumibles'),
    path('enemigos/', views.enemigos, name='enemigos'),
    path('iniciar/', views.iniciar_sesion, name='iniciar_sesion'),
    path('flora/', views.flora, name='flora'),
    path('historia/', views.historia, name='historia'),
]