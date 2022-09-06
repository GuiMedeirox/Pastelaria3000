from django.contrib import admin
from core.models import Cliente, Pastel, Pedido, Bebida, BebidaPedida, PastelPedido 
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Pastel)
admin.site.register(Pedido)
admin.site.register(Bebida)
admin.site.register(BebidaPedida)
admin.site.register(PastelPedido)
