from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Pessoa(models.Model):
    class Meta:
        abstract = True

    nome = models.CharField(max_length=200, verbose_name=u'Nome', null=False, blank=False)
    email = models.EmailField(max_length=200, verbose_name=u'E-mail', null=True, blank=True)
    data_nascimento = models.DateField(verbose_name=u'Data de Nascimento', null=True, blank=True)

    # Endereço
    endereco_logradouro_tipo = models.CharField(max_length=50, null=True, blank=True, verbose_name=u"Tipo de Logradouro")
    endereco_logradouro = models.CharField(max_length=200, null=True, blank=True, verbose_name=u'Logradouro')
    endereco_bairro = models.CharField(max_length=200, null=True, blank=True, verbose_name=u'Bairro')
    endereco_numero = models.CharField(max_length=5, default=u'S/N', null=True, blank=True, verbose_name=u'Número')
    endereco_complemento = models.CharField(max_length=100, null=True, blank=True, verbose_name=u'Complemento')
    endereco_referencia = models.CharField(max_length=100, null=True, blank=True, verbose_name=u'Referência')
    endereco_cidade = models.CharField(max_length=100, null=True, blank=True, verbose_name=u'Cidade')
    endereco_estado = models.CharField(max_length=100, null=True, blank=True, verbose_name=u'Estado')

    def __str__(self):
        return self.nome

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

class Dependente(Pessoa):
    pass

class Cliente(Pessoa):
    vip = models.BooleanField(verbose_name=u'VIP?', default=0)
    pontos_fidelidade = models.PositiveIntegerField(verbose_name=u'Pontos de Fidelidade', default=0)
    dependentes = models.ManyToManyField(Dependente, verbose_name="Dependetes")


class CopiaFisica(models.Model):
    class Meta:
        abstract = True

    filme = models.ForeignKey(Filme)
    fabricante = models.ForeignKey(Fabricante)
    unidades = models.PositiveIntegerField(verbose_name=u'Quantidade de unidades', default=0)
    em_estoque = models.PositiveIntegerField(verbose_name=u'Em estoque', default=0)
    duplo = models.BooleanField(default=False)
    dual_layer = models.BooleanField(default=False)


class DVD(CopiaFisica):
    regiao = models.PositiveIntegerField(default=4) # Região 4 = Brasil


class BluRay(CopiaFisica):
    pass