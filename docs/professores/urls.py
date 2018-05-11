from django.urls import path
from professores.views import *

urlpatterns = [

    path('', listaProfessor),
    path('cadastrarProfessor/', cadastrarProfessor),
    path('remover/<int:id>', removerProfessor),
    path('alterar/<int:id>', alterarProfessor),
    
]