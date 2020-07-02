from django.db import models

# Create your models here.

class Produtos(models.Model):
    nome = models.CharField(max_length = 255)
    descricao = models.CharField(max_length = 255)

class Fornecedor(models.Model):
    nome = models.CharField(max_length = 255)
    endereco = models.CharField(max_length = 255)
    produtos = models.ForeignKey(Produtos, on_delete=models.CASCADE)

class Categoria(models.Model):
    descricao= models.CharField(max_length = 255)

