from django.urls import path
from .views import index, cadastro, lista

urlpatterns = [
    path('', index),
    path('cadastro/', cadastro),
    path('lista/', lista),
]
