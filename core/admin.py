from django.contrib import admin
from core.models import Cliente, Tamanho, Pizza, Ingrediente, Fornada, Pedido, Bebida, BebidaPedida, PizzaPedida, PizzaPedida_has_Ingrediente 
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Tamanho)
admin.site.register(Pizza)
admin.site.register(Ingrediente)
admin.site.register(Fornada)
admin.site.register(Pedido)
admin.site.register(Bebida)
admin.site.register(BebidaPedida)
admin.site.register(PizzaPedida)
admin.site.register(PizzaPedida_has_Ingrediente)