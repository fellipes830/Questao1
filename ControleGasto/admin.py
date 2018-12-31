from datetime import timedelta
from django.contrib import admin
from django.utils.timezone import now
from ControleGasto.models import Despesa



class DespesaAdmin(admin.ModelAdmin):
     list_display = ('data_criacao','tipo_despesa','descricao','forma_pagamento','vencimento','quitado','vencendo')
     list_filter = ('vencimento','quitado',)

     def vencendo(self,obj):
     	return obj.vencimento >= now().date() - timedelta(days=2)


     vencendo.short_description = 'venceu?'
     vencendo.boolean = True

    
    




admin.site.register(Despesa,DespesaAdmin)
