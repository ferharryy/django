from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    dataCadastro = models.DateField()
    ativo = models.BooleanField()