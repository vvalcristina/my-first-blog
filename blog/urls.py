from django.urls import path
from .views import Criar,Lista

urlpatterns = [
    path('cadastro/', Criar.as_view(), name='cadastro'),
    path('lista/', Lista.as_view(), name='lista'),
]
