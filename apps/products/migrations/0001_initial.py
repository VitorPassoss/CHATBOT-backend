# Generated by Django 4.0 on 2023-06-23 05:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_reason', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=10)),
                ('cnpj', models.CharField(blank=True, max_length=14, validators=[django.core.validators.RegexValidator(code='invalid_cpf_cnpj', message='CPF ou CNPJ inválido', regex='^(\\d{3}\\.?\\d{3}\\.?\\d{3}-?\\d{2})$|^(\\d{2}\\.?\\d{3}\\.?\\d{3}/?\\d{4}-?\\d{2})$')], verbose_name='CPF/CNPJ')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('quantity', models.DecimalField(blank=True, decimal_places=3, max_digits=21, null=True)),
                ('measure', models.CharField(blank=True, choices=[('UN', 'unit'), ('KG', 'kilogram'), ('LT', 'Liter')], max_length=2, null=True)),
                ('supplie_fk', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='products.supplier')),
            ],
        ),
    ]
