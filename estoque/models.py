from django.db import models
from midia.models import Filme

class Fabricante(models.Model):
    nome_fantasia = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=50, verbose_name=u'CNPJ', null=True, blank=True)

    def __str__(self):
        return self.nome_fantasia

class CopiaFisica(models.Model):
    class Meta:
        abstract = True
        unique_together = ['fabricante', 'lote']

    filme = models.ForeignKey(Filme)
    fabricante = models.ForeignKey(Fabricante)
    lote = models.PositiveIntegerField()
    unidades = models.PositiveIntegerField(verbose_name=u'Quantidade de unidades', default=0)
    em_estoque = models.PositiveIntegerField(verbose_name=u'Em estoque', default=0)
    duplo = models.BooleanField(default=False)
    dual_layer = models.BooleanField(default=False)


class DVD(CopiaFisica):
    regiao = models.PositiveIntegerField(default=4) # Região 4 = Brasil


class BluRay(CopiaFisica):
    pass