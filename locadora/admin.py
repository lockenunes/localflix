from django.contrib import admin
from .models import *


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



admin.site.register(Diretor, DiretorAdmin)
admin.site.register(Ator, AtorAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Filme, FilmeAdmin)
admin.site.register(DVD)
admin.site.register(BluRay)
admin.site.register(Cliente)
admin.site.register(Fabricante)


