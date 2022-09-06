from django.shortcuts import render
from core.models import Pastel, Bebida
# Create your views here.

def index(request):
  saborPastel = Pastel.objects.all()  
  bebida = Bebida.objects.all()
  context = {
    'saborPastel': saborPastel,
    'bebida': bebida
  }
  return render(request, 'index.html', context)

def gerenciarPedidos(request): 
  return render(request, 'gerenciarPedidos.html')