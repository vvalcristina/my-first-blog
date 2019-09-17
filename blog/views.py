from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        "title": "Página principal",
        "content": "Bem-vindo a página principal"
    }
    return render(request, "cadastro/index.html", context)

def cadastro(request):
    context = {
        "title": "Página sobre",
        "content": "Bem-vindo a página sobre"
    }
    return render(request, "cadastro/cadastro.html", context)

def lista(request):
    context = {
        "title": "Página de contato",
        "content": "Bem-vindo a página de contato"
    }
    return render(request, "cadastro/lista.html", context)
