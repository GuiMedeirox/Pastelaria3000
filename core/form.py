from django.forms import ModelForm
from core.models import *

class pastelForm(ModelForm):
  class Meta: 
    model = Pastel
    fields = ["sabor","preco","ingrediente"]

class bebidaForm(ModelForm):
  class Meta: 
    model = Bebida
    fields = ["nomeBebida","preco","descricao"]    