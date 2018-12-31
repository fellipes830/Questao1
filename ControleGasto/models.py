from django.db import models
from django.utils.datetime_safe import datetime
from datetime import timedelta
import datetime


class Despesa(models.Model):
    REMEDIO = 'RM'
    ROUPAS = 'RP'
    ALIMENTACAO = 'AL'
    EDUCACAO = 'ED'
    TRANSPORTE = 'TP'
    OUTROS = 'OU'

    tipo_despesa_choices = (
        ( REMEDIO,'Remedio'),
        (ROUPAS ,'Roupas'),
        (ALIMENTACAO ,'Alimentacao'),
        (EDUCACAO ,'Educacao'),
        (TRANSPORTE, 'Transporte'),
        (OUTROS ,'Outros'),

    )
    DINHEIRO = 'DN'
    CARTAO_DE_CREDITO = 'CC'
    CARTAO_DE_DEBITO = 'CD'
    CARTAO_CREDIARIO = 'CCR'
    CHEQUE = 'CH'

    forma_pagamento_choices = (
        (DINHEIRO, 'Dinheiro'),
        (CARTAO_DE_CREDITO,'Cartão de Crédito'),
        (CARTAO_DE_DEBITO, 'Cartão de Débito'),
        (CARTAO_CREDIARIO, 'Cartao de Crediário'),
        (CHEQUE, 'Cheque'),
    )


    data_criacao = models.CharField(max_length=20)
    tipo_despesa = models.CharField(max_length=20,choices = tipo_despesa_choices)
    descricao = models.CharField(max_length=100)
    forma_pagamento = models.CharField(max_length=30,choices = forma_pagamento_choices)
    vencimento = models.DateField()
    quitado = models.BooleanField()

    class Meta:

        ordering = ( '-vencimento','forma_pagamento')

