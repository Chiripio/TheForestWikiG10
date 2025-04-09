from django.urls import path
from . import views

urlpatterns = [
    path('', views.menuprincipal, name='menuprincipal'),  # Ruta raíz como 'menuprincipal'
    path('foro/', views.foro, name='foro'),
    path('micuenta/', views.micuenta, name='micuenta'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('recuperar/', views.recuperar_contra, name='recuperar'),
    path('lugares/', views.lugares, name='lugares'),
    path('animales/', views.animales, name='animales'),
    path('armas/', views.armas, name='armas'),
    path('construcciones/', views.construcciones, name='construcciones'),
    path('consumibles/', views.consumibles, name='consumibles'),
    path('enemigos/', views.enemigos, name='enemigos'),
    path('iniciar/', views.iniciar_sesion, name='iniciar_sesion'),  # Vista de login
    path('flora/', views.flora, name='flora'),
    path('historia/', views.historia, name='historia'),

    # ✅ Vista para editar perfil (nueva funcionalidad para la rúbrica)
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),

    # ✅ Ruta para cerrar sesión correctamente
    path('cerrar/', views.cerrar_sesion, name='cerrar_sesion'),
]