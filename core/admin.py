from django.contrib import admin
from core.models import Cliente, Tamanho, Pizza, Fornada, Pedido, Bebida, BebidaPedida, PizzaPedida 
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Tamanho)
admin.site.register(Pizza)

admin.site.register(Fornada)
admin.site.register(Pedido)
admin.site.register(Bebida)
admin.site.register(BebidaPedida)
admin.site.register(PizzaPedida)
