from django.contrib import admin
from .models import *


class FabricanteAdmin(admin.ModelAdmin):
	list_display = ['nome_fantasia', 'cnpj', ]
	search_fields = ['nome_fantasia', 'cnpj', ]


class DVDAdmin(admin.ModelAdmin):
	list_display = ['get_filme_titulo', 'lote', 'duplo', 'dual_layer', ]
	search_fields = ['filme__titulo', 'lote']

	def get_filme_titulo(self, obj):
		return obj.filme.titulo

	get_filme_titulo.short_description = u'Filme'


class BlueRayAdmin(DVDAdmin):
	"""
	Itens são exibidos da mesma forma definada em DVDAdmin.
	Campos de busca são os mesmos.
	"""
	pass

admin.site.register(Fabricante, FabricanteAdmin)
admin.site.register(DVD, DVDAdmin)
admin.site.register(BluRay, BlueRayAdmin)