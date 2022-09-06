from django.shortcuts import render
from core.models import Pastel, Bebida, Tamanho
# Create your views here.

def index(request):
 
  saborPastel = Pastel.objects.all()  
  bebida = Bebida.objects.all()
  tamanho = Tamanho.objects.all()
  context = {
    'saborPastel': saborPastel,
    'bebida': bebida,
    'tamanho': tamanho,
  }  
  return render(request, 'index.html', context)

def gerenciarPedidos(request): 
  return render(request, 'gerenciarPedidos.html')