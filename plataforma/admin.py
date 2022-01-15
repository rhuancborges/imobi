from django.contrib import admin
from .models import Imagem, Cidade, DiasVisita, Horario, Imovei, Visitas

# Registra as models na página do admin
@admin.register(Imovei)
class ImoveiAdmin(admin.ModelAdmin):
        list_display = ('rua', 'valor', 'quartos', 'tamanho', 'cidade', 'tipo')
        list_editable = ('valor', 'tipo')
        list_filter = ('cidade', 'tipo')

admin.site.register(Imagem)
admin.site.register(Cidade)
admin.site.register(DiasVisita)
admin.site.register(Horario)
admin.site.register(Visitas)
