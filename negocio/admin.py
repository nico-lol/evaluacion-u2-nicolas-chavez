from django.contrib import admin
from .models import Equipo, Arriendo

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'disponible')
    search_fields = ('nombre', 'marca')
    list_filter = ('disponible',)

@admin.register(Arriendo)
class ArriendoAdmin(admin.ModelAdmin):
    list_display = ('equipo', 'fecha_inicio', 'valor', 'fecha_fin', 'cliente')
    search_fields = ('equipo__nombre', 'cliente')
    list_filter = ('fecha_inicio', 'fecha_fin')
