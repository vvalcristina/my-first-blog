# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse_lazy

class Inscricao(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    idade = models.IntegerField()
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True)
    criado= models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        ordering = ('criado',)

    def __str__(self):
        return self.nome
