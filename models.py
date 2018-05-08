from django.db import models
from django.utils.translation import gettext as _

class DataHoraCriacaoMixin(models.Model):
    class Meta:
        abstract = True

    datahora_criacao = models.DateTimeField(auto_now_add=True)


class DataHoraEdicaoMixin(models.Model):
    class Meta:
        abstract = True

    datahora_edicao = models.DateTimeField(auto_now=True)

class SlugMixin(models.Model):
    class Meta:
        abstract = True

    slug = models.SlugField(unique=True, verbose_name=_("Slug"), blank=True, max_length=254)

class TelefoneMixin(models.Model):
    class Meta:
        abstract = True

    telefone = models.CharField(
        _('Número de Telefone'),
        max_length=20,
        blank=True,
        null=True
    )

class EnderecoMixin(models.Model):
    class Meta:
        abstract = True

    cep = models.CharField(max_length=20, blank=True, verbose_name=_('CEP'))
    pais = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Pais'))
    estado = models.CharField(max_length=255, blank=True, verbose_name=_('Estado'))
    cidade = models.CharField(max_length=255, blank=True, verbose_name=_('Cidade'))
    bairro = models.CharField(max_length=255, blank=True, verbose_name=_('Bairro'))
    rua = models.CharField(max_length=255, blank=True, verbose_name=_('Rua'))
    numero = models.IntegerField(blank=True, null=True, verbose_name=_('Número'))
    complemento = models.CharField(max_length=255, blank=True, verbose_name=_('Complemento'), null=True)

class AtivoMixin(models.Model):
    class Meta:
        abstract = True

    ativo = models.BooleanField(verbose_name=_("Ativo"), default=True)