from django.contrib import admin
from .models import Equipo, Arriendo

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'arrendado')
    search_fields = ('nombre', 'marca')
    list_filter = ('arrendado',)

@admin.register(Arriendo)
class ArriendoAdmin(admin.ModelAdmin):
    list_display = ('equipo', 'fecha_inicio', 'valor_peso', 'fecha_fin', 'cliente')
    search_fields = ('equipo__nombre', 'cliente')
    list_filter = ('fecha_inicio', 'fecha_fin')

    @admin.display(description='Valor (pesos)', ordering='valor')
    def valor_peso(self, obj):
        return f"${obj.valor:,}".replace(",", ".")