from django.contrib import admin
from core.models import Cliente, Tamanho, Pastel, Pedido, Bebida, BebidaPedida, PastelPedido
from django.apps import apps

# Register your models here.

models = apps.get_models()
for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
