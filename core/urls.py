from django.urls import path
from . import views

urlpatterns = [
    # Página principal
    path('', views.menuprincipal, name='menuprincipal'),

    # Navegación
    path('foro/', views.foro, name='foro'),
    path('lugares/', views.lugares, name='lugares'),
    path('animales/', views.animales, name='animales'),
    path('armas/', views.armas, name='armas'),
    path('construcciones/', views.construcciones, name='construcciones'),
    path('consumibles/', views.consumibles, name='consumibles'),
    path('enemigos/', views.enemigos, name='enemigos'),
    path('flora/', views.flora, name='flora'),
    path('historia/', views.historia, name='historia'),
    path('direccion/', views.direccion, name='direccion'),  # ✅ Vista interna del mapa
    path('logros/', views.logros, name='logros'),  # ✅  vista de logros

    # Usuario
    path('micuenta/', views.micuenta, name='micuenta'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('recuperar/', views.recuperar_contra, name='recuperar'),
    path('iniciar/', views.iniciar_sesion, name='iniciar_sesion'),
    path('cerrar/', views.cerrar_sesion, name='cerrar_sesion'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('eliminar_usuario/', views.eliminar_usuario, name='eliminar_usuario'),

    # Vista de administrador
    path('admin_visual/', views.admin_visual, name='admin_visual'),
]