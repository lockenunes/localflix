from django.contrib import admin

from midia.forms import FilmeForm
from .models import Diretor, Categoria, Ator, Filme


class DiretorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'especialidade', 'numero_de_oscar', ]
    search_fields = ['nome', 'email', ]
    list_filter = ['especialidade', 'numero_de_oscar', ]


class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nome']


class AtorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'numero_de_oscar', ]
    search_fields = ['nome', 'email', ]
    list_filter = ['numero_de_oscar', ]


class FilmeAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'ano_producao', 'numero_de_oscar', ]
    search_fields = ['titulo', ]
    list_filter = ['diretor', 'atores', 'categoria', 'ano_producao', 'numero_de_oscar', ]
    form = FilmeForm


admin.site.register(Diretor, DiretorAdmin)
admin.site.register(Ator, AtorAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Filme, FilmeAdmin)