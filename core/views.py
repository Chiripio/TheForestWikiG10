from django.shortcuts import render

def menuprincipal(request):
    return render(request, 'core/menuprincipal_wiki.html')

def foro(request):
    return render(request, 'core/forowiki.html')

def micuenta(request):
    return render(request, 'core/micuentatf.html')

def registrarse(request):
    return render(request, 'core/registrase_wiki.html')

def login(request):
    return render(request, 'core/inicio_sesion_wiki.html')

def recuperar_contra(request):
    return render(request, 'core/recuperarcontra.html')

def lugares(request):
    return render(request, 'core/Lugarestf.html')

def animales(request):
    return render(request, 'core/animales.html')

def armas(request):
    return render(request, 'core/Armas.html')

def construcciones(request):
    return render(request, 'core/construcciones.html')

def consumibles(request):
    return render(request, 'core/consumibles.html')

def enemigos(request):
    return render(request, 'core/Enemigos.html')

def iniciar_sesion(request):
    return render(request, 'core/inicio_sesion_wiki.html')

def flora(request):
    return render(request, 'core/flora.html')

def historia(request):
    return render(request, 'core/historia.html')

