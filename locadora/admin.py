from django.contrib import admin
from .models import *


class ClienteAdmin(admin.ModelAdmin):
	list_display = ['nome', 'pontos_fidelidade', 'vip', ]
	search_fields = ['nome', ]

	def get_quantidade_dependentes(self, obj):
		"""
		Método para calcular o número de dependentes para exibir na listagem de clientes.
		:param obj: Cliente Model
		:return: Quantidade de dependentes alocados para o responsável
		"""
		pass

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Dependente)

