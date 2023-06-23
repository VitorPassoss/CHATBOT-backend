from django.db import models
from django.core.validators import RegexValidator

class Supplier(models.Model):
    social_reason = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    street = models.CharField(max_length=255)  # Nome da rua
    postal_code = models.CharField(max_length=10)  
    cnpj = models.CharField(
        verbose_name="CPF/CNPJ",
        max_length=14,
        validators=[
            RegexValidator(
                regex=r"^(\d{3}\.?\d{3}\.?\d{3}-?\d{2})$|^(\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2})$",
                message="CPF ou CNPJ inválido",
                code="invalid_cpf_cnpj",
            )
        ],
        blank=True,
    )