from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    
    path('gerenciarPasteis', gerenciarPasteis, name="gerenciar"),
    path('editarPastel/<int:id>', EditarPastel, name="editarPastel"),
    path('delete/<int:id>', DeletarPastel, name="deletarPastel"),

    path('gerenciarBebidas', gerenciarBebidas, name="gerenciarBebidas"),
    path('editarBebida/<int:id>', EditarBebida, name="editarBebida"),
    path('deleteBebida/<int:id>', DeletarBebida, name="deletarBebida"),
  
]