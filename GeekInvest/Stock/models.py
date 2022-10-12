# <------------------Importar Bibliotecas-------------->
from statistics import mode
from django.db import models
import uuid

# <--------------Base De dados Do Model-------------------------->
class stock_models(models.Model):
    TIPO_CHOISE = [
        ('acao', 'Ação'),
        ('fii', 'Fundo de Investimento Imobiliário'),
        ('bdr', 'Brazilian Depositary Receipts')
    ]

    id = models.UUIDField(
        default=uuid.uuid4,
        null=False,
        blank=False
    )
    ticket = models.CharField(
        max_length=10,
        primary_key=True,
        null=False,
        blank=False
    )
    nome = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    tipo = models.CharField(
        max_length=5,
        choices=TIPO_CHOISE,
        null=False,
        blank=False
    )
    cnpj = models.CharField(
        max_length=25,
        null=True,
        blank=True
    )
    setor = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    sub_setor = models.CharField(
        max_length=25,
        null=True,
        blank=True
    )
