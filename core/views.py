from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from core.models import Usuario, RolUsuario
from django.contrib.auth.models import User,Group
# -------------------------
# VISTAS DE NAVEGACIÓN
# -------------------------

def menuprincipal(request):
    return render(request, 'core/menuprincipal_wiki.html')

def foro(request):
    return render(request, 'core/forowiki.html')

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

def flora(request):
    return render(request, 'core/flora.html')

def historia(request):
    return render(request, 'core/historia.html')

# -------------------------
# VISTAS DE USUARIO
# -------------------------

# Vista: Perfil del usuario
def micuenta(request):
    if not request.session.get('usuario_id'):
        messages.warning(request, '⚠ Debes iniciar sesión para acceder a tu cuenta.')
        return redirect('iniciar_sesion')
    user = User.objects.get(id=request.session.get('usuario_id'))
    return render(request, 'core/micuentatf.html',{'user':user})

# Vista: Registro de usuario
def registrarse(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm_password')

        if password != confirm:
            messages.error(request, "❌ Las contraseñas no coinciden.")
            return render(request, 'core/registrase_wiki.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "❌ El correo ya está registrado.")
            return render(request, 'core/registrase_wiki.html')

        try:
            rol_default = Group.objects.get(name="Cliente")
        except Group.DoesNotExist:
            messages.error(request, "❌ Error: El rol 'Cliente' no existe. Crea uno desde el administrador.")
            return render(request, 'core/registrase_wiki.html')
        # Creación del Usuario en BD.
        nuevo_usuario = User(
            username=email,
            email=email,
            first_name=first_name,
            last_name=lastname,
            
        )
        nuevo_usuario.set_password(password)
        nuevo_usuario.save()
        nuevo_usuario.groups.add(rol_default)

        messages.success(request, "✅ ¡Cuenta creada exitosamente! Ahora puedes iniciar sesión.")
        return redirect('iniciar_sesion')

    return render(request, 'core/registrase_wiki.html')

# Vista: Recuperar contraseña
def recuperar_contra(request):
    return render(request, 'core/recuperarcontra.html')

# Vista: Iniciar sesión
def iniciar_sesion(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            usuario = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, '❌ No existe un usuario con ese correo.')
            return redirect('iniciar_sesion')
        if usuario.check_password(password):
            request.session['usuario_id'] = usuario.id
            request.session['usuario_nombre'] = usuario.get_full_name() 
            request.session['usuario_rol'] = ""
            

            if usuario.username.lower() == "admin":
                return redirect('micuenta')
            else:
                return redirect('menuprincipal')
        else:
            messages.error(request, '❌ Contraseña incorrecta.')
            return redirect('iniciar_sesion')
    
    return render(request, 'core/inicio_sesion_wiki.html')

# Vista: Cerrar sesión
def cerrar_sesion(request):
    request.session.flush()
    messages.success(request, "✅ Has cerrado sesión correctamente.")
    return redirect('iniciar_sesion')

# Vista: Editar perfil
def editar_perfil(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        messages.warning(request, '⚠ Debes iniciar sesión para editar tu perfil.')
        return redirect('iniciar_sesion')

    try:
        usuario = Usuario.objects.get(id=usuario_id)
    except Usuario.DoesNotExist:
        messages.error(request, '❌ Usuario no encontrado.')
        return redirect('menuprincipal')

    if request.method == 'POST':
        nuevo_nombre = request.POST.get('nombre')
        nuevo_email = request.POST.get('email')
        nueva_password = request.POST.get('nueva_password')

        # Validar que el nuevo email no esté en uso por otro usuario
        if Usuario.objects.exclude(id=usuario.id).filter(email=nuevo_email).exists():
            messages.error(request, "❌ Ya existe un usuario con ese correo.")
            return render(request, 'core/editar_perfil.html', {'usuario': usuario})

        # Guardar cambios
        usuario.nombre = nuevo_nombre
        usuario.email = nuevo_email
        if nueva_password:
            usuario.password = make_password(nueva_password)
        usuario.save()

        # Actualizar sesión
        request.session['usuario_nombre'] = nuevo_nombre

        messages.success(request, "✅ Perfil actualizado correctamente.")
        return redirect('micuenta')

    return render(request, 'core/editar_perfil.html', {'usuario': usuario})