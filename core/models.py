from django.db import models

# Create your models here.

class Cliente(models.Model):
  idCliente = models.IntegerField(primary_key=True)
  nome = models.CharField('Nome', max_length=255) 
  telefone = models.CharField('Telefone', max_length=255)
  endereco = models.CharField('Endereço', max_length=255)

  def __str__(self):
    return self.nome


class Tamanho(models.Model):
  idTamanho = models.IntegerField(primary_key=True)
  nome = models.CharField('Nome', max_length=255)
  desconto = models.FloatField()

  def __str__(self):
    return self.nome


class Pizza(models.Model):
  idPizza = models.IntegerField(primary_key=True)
  nome = models.CharField('Nome', max_length=255)
  precoBase = models.FloatField()
  def __str__(self):
    return self.nome



class Fornada(models.Model):
  idFornada = models.IntegerField(primary_key=True)
  numFornada = models.IntegerField()
  qtdPizzas = models.IntegerField()
  def __str__(self):
    return self.idFornada

class Pedido(models.Model):
  idPedido = models.IntegerField(primary_key=True)
  idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
  idFornada = models.ForeignKey(Fornada, on_delete=models.CASCADE)
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

class PizzaPedida(models.Model):
  idPizzaPedida = models.IntegerField(primary_key=True)
  idPedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
  idPizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
  idTamanho = models.ForeignKey(Tamanho, on_delete=models.CASCADE) 
  quantidade = models.IntegerField()
  def __str__(self):
    return self.idPizzaPedida

  
  class Meta: 
    unique_together = ('idPizzaPedida', 'idIngrediente')
  