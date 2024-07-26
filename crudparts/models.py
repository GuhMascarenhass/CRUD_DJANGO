from django.db import models


class Crudparts(models.Model):
    cod = models.CharField(
        verbose_name="Código", primary_key=True, max_length=10, blank=False, null=False
    )
    description = models.CharField(
        verbose_name="Descrição", max_length=50, blank=False, null=False
    )
    equipamento = models.CharField(
        verbose_name="Equipamento", max_length=50, blank=False, null=False
    )
