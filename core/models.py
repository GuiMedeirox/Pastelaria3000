from django.db import models

# Create your models here.

class Cliente(models.Model):
  idCliente = models.IntegerField(primary_key=True)
  nome = models.CharField('Nome', max_length=255) 
  telefone = models.CharField('Telefone', max_length=255)
  endereco = models.CharField('Endereço', max_length=255)

  def __str__(self):
    return self.nome


class Pastel(models.Model):
  idPastel = models.IntegerField(primary_key=True)
  sabor = models.CharField('Sabor', max_length=255, default=None)
  precoBase = models.FloatField()
  def __str__(self):
    return self.sabor



class Pedido(models.Model):
  idPedido = models.IntegerField(primary_key=True)
  idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
  dataHora = models.DateTimeField()
  def __str__(self):
    return self.idPedido

class Bebida(models.Model):
  idBebida = models.IntegerField(primary_key=True)
  nome = models.CharField('Nome', max_length=255)
  preco = models.FloatField()
  def __str__(self):
    return self.nome

class BebidaPedida(models.Model):
  idPedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
  idBebida = models.ForeignKey(Bebida, on_delete=models.CASCADE)
  quantidade = models.IntegerField()
  def __str__(self):
    return self.idBebida

  class Meta:
    unique_together = ('idBebida','idPedido')  

class PastelPedido(models.Model):
  idPastelPedido = models.IntegerField(primary_key=True)
  idPedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
  idPastel = models.ForeignKey(Pastel, on_delete=models.CASCADE)
  quantidade = models.IntegerField()
  def __str__(self):
    return self.idPastelPedido


  