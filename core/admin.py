from django.contrib import admin
from .models import Usuario, RolUsuario

# 🧑‍💻 Personalización del panel de administración para el modelo Usuario
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'rol')  # Columnas visibles
    search_fields = ('nombre', 'email')        # Campos buscables
    list_filter = ('rol',)                     # Filtro lateral por rol

# 🧱 Personalización del panel para RolUsuario (opcional pero útil)
class RolUsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre',)                 # Muestra solo el nombre del rol
    search_fields = ('nombre',)                # Permite buscar por nombre

# 📌 Registro de modelos con sus configuraciones personalizadas
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(RolUsuario, RolUsuarioAdmin)