from django.db import models
from midia.models import Filme

class Fabricante(models.Model):
    nome_fantasia = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=50, verbose_name=u'CNPJ', null=True, blank=True)

    # Endereço
    endereco_logradouro_tipo = models.CharField(max_length=50, null=True, blank=True, verbose_name=u"Tipo de Logradouro")
    endereco_logradouro = models.CharField(max_length=200, null=True, blank=True, verbose_name=u'Logradouro')
    endereco_bairro = models.CharField(max_length=200, null=True, blank=True, verbose_name=u'Bairro')
    endereco_numero = models.CharField(max_length=5, default=u'S/N', null=True, blank=True, verbose_name=u'Número')
    endereco_complemento = models.CharField(max_length=100, null=True, blank=True, verbose_name=u'Complemento')
    endereco_referencia = models.CharField(max_length=100, null=True, blank=True, verbose_name=u'Referência')
    endereco_cidade = models.CharField(max_length=100, null=True, blank=True, verbose_name=u'Cidade')
    endereco_estado = models.CharField(max_length=100, null=True, blank=True, verbose_name=u'Estado')


class CopiaFisica(models.Model):
    class Meta:
        abstract = True

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


