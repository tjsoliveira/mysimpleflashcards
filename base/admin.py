from django.contrib import admin
from base.models import Disciplina, Baralho, Carta

# Register your models here.
@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    pass

@admin.register(Baralho)
class BaralhoAdmin(admin.ModelAdmin):
   pass

@admin.register(Carta)
class CartaAdmin(admin.ModelAdmin):

   exclude = ('visto_quando', 'sera_visto_em', )