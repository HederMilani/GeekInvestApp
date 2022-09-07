from django.db import models
import uuid

class InstituicaoModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=False
    )
    nome = models.CharField(
        max_length=50,
        null=True,
        blank=False
    )
    pais = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    cnpj = models.CharField(
        max_length=25,
        null=True,
        blank=True
    )
