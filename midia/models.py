from django.db import models
from comum.models import Pessoa
from django.core.validators import MinValueValidator, MaxValueValidator


class Diretor(Pessoa):
    class Meta:
        verbose_name = u'Diretor'
        verbose_name_plural = u'Diretores'

    especialidade = models.CharField(max_length=200, verbose_name=u'Especialidade', null=False, blank=False)
    numero_de_oscar = models.IntegerField(verbose_name=u'Quantidade de Oscar', default=0, null=False, blank=False)


class Ator(Pessoa):
    class Meta:
        verbose_name = u'Ator'
        verbose_name_plural = u'Atores'

    numero_de_oscar = models.IntegerField(verbose_name=u'Quantidade de Oscar', default=0, null=False, blank=False)


class Categoria(models.Model):
    class Meta:
        verbose_name = u'Categoria'
        verbose_name_plural = u'Categorias'

    nome = models.CharField(max_length=50, verbose_name=u'Nome', null=False, blank=False)

    def __str__(self):
        return self.nome


class Filme(models.Model):
    titulo = models.CharField(max_length=200, verbose_name=u'Título')
    ano_producao = models.PositiveIntegerField(verbose_name=u'Ano de Produção', validators=[MinValueValidator(1980), MaxValueValidator(2016)])
    categoria = models.ForeignKey(Categoria, verbose_name=u'Categoria')
    atores = models.ManyToManyField(Ator, verbose_name=u'Atores')
    diretor = models.ForeignKey(Diretor, verbose_name=u'Diretor')
    numero_de_oscar = models.IntegerField(verbose_name=u'Quantidade de Oscar', default=0, null=False, blank=False)

    def __str__(self):
        return self.titulo