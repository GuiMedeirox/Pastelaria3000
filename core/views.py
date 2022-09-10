from django.shortcuts import render, redirect
from core.models import *
from core.form import pastelForm, bebidaForm
# Create your views here.

def index(request):
  pasteis = Pastel.objects.all()
  bebidas = Bebida.objects.all()
  pacote = {'pasteis':pasteis, 'bebidas':bebidas}
  return render(request, 'index.html', pacote)


# CRUD dos Pastéis

def gerenciarPedidos(request): 
  pasteis = Pastel.objects.all()
  formPastel = pastelForm(request.POST or None)
  if formPastel.is_valid():
    formPastel.save()
    return redirect("index")
  pacote = {'formPastel':formPastel, 'pasteis':pasteis}
  return render(request, 'gerenciarPedidos.html', pacote) 

def EditarPastel(request, id):
  pasteis = Pastel.objects.get(pk=id)
  formPastel = pastelForm(request.POST or None, instance=pasteis)
  if formPastel.is_valid() :
    formPastel.save()
    return redirect("index")    
  pacote = {"formPastel": formPastel}
  return render(request, "editarPastel.html", pacote)

def DeletarPastel(request,id):
  pasteis = Pastel.objects.get(pk=id)
  pasteis.delete()
  return redirect("index")

# CRUD das Bebida


def gerenciarBebidas(request): 
  bebidas = Bebida.objects.all()
  formBebida = bebidaForm(request.POST or None)
  if formBebida.is_valid():
    formBebida.save()
    return redirect("index")
  pacote = {'formBebida':formBebida, 'bebidas':bebidas}
  return render(request, 'gerenciarBebidas.html', pacote) 

def EditarBebida(request, id):
  bebidas = Bebida.objects.get(pk=id)
  formBebida = bebidaForm(request.POST or None, instance=bebidas)
  if formBebida.is_valid() :
    formBebida.save()
    return redirect("index")    
  pacote = {"formBebida": formBebida}
  return render(request, "editarBebida.html", pacote)

def DeletarBebida(request,id):
  bebidas = Bebida.objects.get(pk=id)
  bebidas.delete()
  return redirect("index")
