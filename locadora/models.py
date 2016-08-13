from django.db import models
from comum.models import Pessoa


class Dependente(Pessoa):
    pass

class Cliente(Pessoa):
    vip = models.BooleanField(verbose_name=u'VIP?', default=0)
    pontos_fidelidade = models.PositiveIntegerField(verbose_name=u'Pontos de Fidelidade', default=0)
    dependentes = models.ManyToManyField(Dependente, verbose_name="Dependetes")