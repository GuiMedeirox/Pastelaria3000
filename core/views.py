from django.shortcuts import render, redirect
from core.models import *
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


def FazerPedido(request):
    if request.is_valid():
        Pedido.save()
         

def create(request):
    
    
  if request.method=="POST":
      sabor=request.POST['sabor']
      tamanho=request.POST['tamanho']
      quantidadePastel=request.POST['quantidadePastel']
      bebida=request.POST['bebida']
      quantidadeBebida=request.POST['quantidadeBebida']
      obj=Pedido.create(idPastel=sabor,idTamanho=tamanho,quantidadePastel=quantidadePastel,bebida=bebida,quantidadeBebida=quantidadeBebida)
      obj.save()
      return redirect("gerenciar")   
  return render(request, 'gerenciarPedidos.html')