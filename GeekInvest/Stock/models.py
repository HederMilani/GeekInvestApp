# <-------------Importar Bibliotecas------------->
from django.db import models
import uuid

class Stock(models.Model):
    TIPO_CHOISE = [
        ('acao', 'Ação'),
        ('fii', 'Fundo Investimento Imobiliário'),
        ('bdr', 'Brazilian Depositary Receipts')
    ]

    id = models.UUIDField(
        default=uuid.uuid4,
        null=False,
        blank=False
    ),
    ticket = models.CharField(
        primary_key=True,
        max_length=10,
        null=False,
        blank=False
    ),
    nome = models.CharField(
        max_length=50,
        null=True,
        blank=False
    ),
    tipo = models.CharField(
        max_length=20,
        choices=TIPO_CHOISE,
        null=True,
        blank=False
    ),
    cnpj = models.CharField(
        max_length=25,
        null=True,
        blank=True
    )
