from email.policy import default
from django.db import models

# Create your models here.

# class Cliente(models.Model):
#   nome = models.CharField('Nome', max_length=255) 
#   telefone = models.CharField('Telefone', max_length=255)
#   endereco = models.CharField('Endereço', max_length=255)
#   def __str__(self):
#     return self.nome

# class Tamanho(models.Model):
#   tamanho = models.CharField('Tamanho', max_length=255)
#   def __str__(self):
#       return self.tamanho

class Pastel(models.Model):
  sabor = models.CharField('Sabor', max_length=255, blank=True)
  preco = models.FloatField('Preco', default=0, blank=True)
  ingrediente = models.CharField('Ingrediente', max_length=255, blank=True)
  def __str__(self):
      return self.sabor

class Bebida(models.Model):
  nomeBebida = models.CharField('NomeBebida', max_length=255, blank=True) 
  preco = models.FloatField('Preco', default=0, blank=True)
  descricao = models.CharField('Descricao', max_length=255, blank=True)
  def __str__(self):
      return self.nomeBebida


# class Pedido(models.Model):
  # idCliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
  # idPastelPedido = models.ForeignKey('PastelPedido', on_delete=models.CASCADE)
  # idBebidaPedida = models.ForeignKey('BebidaPedida', on_delete=models.CASCADE)
  
  # idPastel = models.ForeignKey('Pastel', on_delete=models.CASCADE)
  # idTamanho = models.ForeignKey('Tamanho', on_delete=models.CASCADE)
  # quantidadePastel = models.IntegerField('Quantia', default=1)
  # idBebida = models.ForeignKey('Bebida', on_delete=models.CASCADE) 
  # quantidadeBebida = models.IntegerField('Quantia', default=1) 
  # dataHora = models.DateTimeField('DataHora', auto_now_add=True)

# class PastelPedido(models.Model):
#   idPastel = models.ForeignKey('Pastel', on_delete=models.CASCADE)
#   idTamanho = models.ForeignKey('Tamanho', on_delete=models.CASCADE)
#   quantia = models.IntegerField('Quantia', default=1)

# class BebidaPedida(models.Model):
#   idBebida = models.ForeignKey('Bebida', on_delete=models.CASCADE) 
#   quantia = models.IntegerField('Quantia', default=1) 
  

