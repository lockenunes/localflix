from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class ProfissionalDoCinema(models.Model):
    class Meta:
        abstract = True

    nome = models.CharField(max_length=200, verbose_name=u'Nome', null=False, blank=False)
    email = models.EmailField(max_length=200, verbose_name=u'E-mail', null=False, blank=False)

    def __str__(self):
        return self.nome

class Diretor(ProfissionalDoCinema):
    class Meta:
        verbose_name = u'Diretor'
        verbose_name_plural = u'Diretores'

    especialidade = models.CharField(max_length=200, verbose_name=u'Especialidade', null=False, blank=False)


class Ator(ProfissionalDoCinema):
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
    ano_producao = models.PositiveIntegerField(verbose_name=u'Data de Produção', validators=[MinValueValidator(1980), MaxValueValidator(2016)])
    categorias = models.ManyToManyField(Categoria, verbose_name=u'Categorias')
    atores = models.ManyToManyField(Ator, verbose_name=u'Atores')
    diretor = models.ForeignKey(Diretor, verbose_name=u'Diretor')

    def __str__(self):
        return self.titulo