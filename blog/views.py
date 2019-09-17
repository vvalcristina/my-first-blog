from django.shortcuts import render
from django.views.generic import CreateView,ListView

from blog.models import Inscricao
from blog.forms import InscricaoForm

def home(request):
    return render(request,'index.html')

class Criar(CreateView):
    template_name= 'cadastro.html'
    model = Inscricao


class Lista(ListView):
    template_name = 'lista.html'
    model = Inscricao
    context_object= 'nome'
